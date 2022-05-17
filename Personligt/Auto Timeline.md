

# Auto Timeline

1. find alle filer med `#timeline`.  Dette skal ske ved at læse linjer fra bunden af. Hvis tagget ikke er der i de nederste 10 linjer, går vi viddere til næste fil.
2. Hvis `#timeline` er fundet:
	1. find i metadata: **dato(er)**, **eventtype?** (kan også findes med antallet af datoer), **Titel** (hvis den ikke er i metadataen, tager vi overskriften/filens navn), **Billeder**? (checker for links til billeder).
	2. Lav en `timeline` block med alle de informationer vi fandt. Eventuel undertekst.
	3. Find andre tags og lav det som eventens "class"
	4. Lav en plads i metadataen til værdien `on_timeline` der er en bool.
3. Ignorer alle filer med metadataen `freeze : true`

#ide