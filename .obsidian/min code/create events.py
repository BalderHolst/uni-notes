from glob import glob

search_threshold = 5
tag = "#tidslinje"

def get_file_list(path):
    files = glob(path+"*.md")
    res = []
    for file in files:
        res.append(file.replace('\\','/'))

    return(res)


def find_image(lines):
    image = ""
    for line in lines:
        pointer = line.find("![")
        if(pointer != -1):
            image = line[line.find(']') + 2:line.find(')')]

        pointer = line.find("![[")
        if(pointer != -1):
            image = line[pointer + 3:line.find(']]')]


    if(len(image) > 0):
        return(image)
    else:
        return(None)

def name(path):
    return(path.split('/')[-1].split('.')[0])



def make_to_digits(num_string,digits):
    while(len(num_string) < digits):           #sætter nuller foran
            num_string = '0' + num_string
    return(num_string[len(num_string)-digits:])

def format_date(in_date):
    if(in_date.find('-') == -1):
        in_date = make_to_digits(in_date,4)
    
    in_date_list = in_date.split('-')
    while(len(in_date_list) < 4):
        in_date_list.append('01')
    
    for d in range(len(in_date_list)):
        while len(in_date_list[d]) < 2:
            in_date_list[d] = '0' + in_date_list[d]


    out_date = ""

    for s in in_date_list : out_date += s + '-'

    return(out_date[:-1])


def get_class(lines):
    
    tags = []

    for l in range(search_threshold):
        if(lines[-l].find('#') >= 0 and lines[-l].find("#timeline") == -1 and lines[-l].find('##') == -1):
            tags.append(lines[-l])
    if(len(tags) > 0):
        return(tags[-1][1:-1])
    else:
        return('default')

def get_metadata(file):
    with open(file,"r") as f: 
            lines=f.readlines() 

    if(lines[0].find("---") != -1):
        i = 1


        keys = ['dato','dato_start','dato_slut','eventtype','titel','image','class','beskrivelse']

        metadata = {}

        for key in keys : metadata[key] = None


        while(lines[i].find("---")):
            line = lines[i]

            key = line[:line.find(':')-1]
            value = line[line.find(':')+2:line.find('\n')]
            
            if(len(key) > 0 and len(value) > 0):
                metadata[key] = value

            i += 1

            if (i > 100):
                print(f"error in metadata in file {name(file)}")

 
        if(metadata['eventtype'] == None):          #finder ud af om det er en event eller en periode
            if(metadata['dato'] != None):
                metadata['eventtype'] = 'event'
            else:
                metadata['eventtype'] = 'periode'
                if(metadata['dato_start'] == None or metadata['dato_slut'] == None): #errorbesked
                    print(f"incorrect metadata in file {name(file)}")
                    quit()

        if(metadata['titel'] == None):
            metadata['titel'] = name(file)

        if metadata['titel'].find('\"') >= 0 : metadata['titel'] = metadata['titel'][1:-1]
        metadata['image'] = find_image(lines)
        metadata['class'] = get_class(lines)

        return(metadata)




    else:
        print(f"incorrect metadata in file {name(file)}")
        quit()

def isOnTimeline(lines):
    for line in lines:
        if(line.find("<span") >= 0):
            return(True)
    return(False)

def make_event_block(metadata):
    l1 =  "\n<span\n"
    l2 =  "      class='ob-timelines'\n"
    l3 = f"      data-date='{format_date(metadata['dato'])}'\n"
    l4 = f"      data-title='{metadata['titel']}'\n"
    l5 = f"      data-class='{metadata['class']}'\n"

    img = f"      data-img='{metadata['image']}'"

    end = f"      data-type='box' >\n"
    
    

    out = [l1,l2,l3,l4,l5]

    if metadata['image'] != None: out.append(img + '\n')

    out.append(end)
    out.append("</span>")

    return(out)

#<span 
#      class='ob-timelines' 
#      data-title='Romantisme' 
#      data-date='1820-01-01-00' 
#      data-end="1850-01-01-00"
#      data-img='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F7%2F78%2FJohan_Christian_Clausen_Dahl_-_Et_skibbrud_ved_den_norske_kyst_-_Statens_Museum_for_Kunst_-_KMS216.jpg&f=1&nofb=1'
#      data-class='red' 
#      data-type='range' 
#      > 
#</span>

def make_period_block(metadata):
    
    l1 =  "\n<span\n"
    l2 =  "      class='ob-timelines'\n"
    l3 = f"      data-title='{metadata['titel']}'\n"
    l4 = f"      data-date='{format_date(metadata['dato_start'])}'\n"
    l5 = f"      data-end=\"{format_date(metadata['dato_slut'])}\"\n"
    l6 = f"      data-class='{metadata['class']}'\n"

    img = f"      data-img='{metadata['image']}'"

    end = f"      data-type='box' >\n"
    
    out = [l1,l2,l3,l4,l5,l6]

    if metadata['image'] != None: out.append(img + '\n')
    if metadata['eventtype'] == 'tid':
        out.append(f"      data-type='background'\n")
    else:
        out.append(f"      data-type='range'\n")

    out.append(end)
    out.append("</span>")

    return(out)


def make_timeline_labels_in_dir(path):

    files = get_file_list(path)


    for file in files:
            
        try:
            with open(file,"r") as f:           #læser filens linjer
                    lines=f.readlines() 


            event = False                       #finder ud af om filen indeholder #timeline
            for i in range(search_threshold):
                if(lines[-i].find(tag) != -1):
                    event = True
                    break

            #print(name(file))

            if (event and isOnTimeline(lines) == False):        #hvis der er en event:
                print(f"adding {name(file)} to timeline")


                metadata = get_metadata(file)

                block = []
                if metadata['eventtype'] == 'event':
                    block = make_event_block(metadata)
                else:
                    block = make_period_block(metadata)

                for l in block:                     #Sætter klump på efter resten af noten
                    lines.append(l)

                with open(file,"w") as f: 
                    f.writelines(lines)

        except UnicodeDecodeError:
            print(f"[{name(file)}] failed")


if __name__ == "__main__":
    make_timeline_labels_in_dir("C:/Users/balde/OneDrive/Documents/Balders Noter/Skolerelevant/")
    print("DONE")
    







        