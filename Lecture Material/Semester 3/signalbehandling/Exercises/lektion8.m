%% Variables
fs = 8000
T = 1/fs

%% In s-domain
s = tf('s');
Hs = 2000*pi / ( 1/(2000*pi) * s^2 + s + 2000 * pi );

%% Impule Inveriant z-transformation
z = tf('z')

%% Impule Inveriant z-transformation
a = [ -1 ];
b = [ 1 -exp(-pi/4) ];
H1 = pi/4 * tf(a, b, T);

a = [ -6283 10613 0 ];
b = [ 1 -2.3028 2.1933 ];
H2 = tf(a, b, T)

Hinvariant = H1 + H2

%% Plot

domain = [10^2.5 10^5]

bode(Hs);
xlim(domain)
hold on
bode(H2);
xlim(domain)
hold off

domain = [0 0.2]
xlim(domain)
impulse(Hs);
hold on
impulse(H2);
xlim(domain)
hold off

