# Filter Transformations
See [[Lektion 1 - Filterfunktioner.pdf#page=53|slide]].

Other types of filters can be designed by transforming them to low-pass filters, determining their order, and then transforming them back.
![[Pasted image 20230914092435.png]]

### Creating a high-pass filter
We can mirror the filter over the cutoff frequency by *dividing the nominated filter* by the cutoff frequency itself ($\omega_{s}$).
$$H_{hp}(s) = H_{lp}(\bar{s})|_{\bar{s} = \frac{1}{s}}$$
![[Pasted image 20230914092721.png|450]]

>[!example]- Example of creating of high-pass filter
>![[Lektion 1 - Filterfunktioner.pdf#page=57]]

Denomering
$$s \rightarrow \frac{s}{\omega_{a}}$$

### Creating a band-pass filter
[[Lektion 1 - Filterfunktioner.pdf#page=66]]

A band pass filer is a combination of a high-pass and a low-pass filter.
$$H_{bp} = H_{lp} \cdot H_{hp}$$
![[Pasted image 20230914094007.png|350]]
$\omega_{a}$: Pass-band width
$\omega_{s}$: Stop-band width
$\omega$: Center-frequency: The middle of the stop-band-frequencies, on a *logarithmic scale*.
$A_{s}$: The filter stop-dampening.

![[Pasted image 20230914094350.png|550]]

**NOTE:** We use the *center-frequency* to nominate the filter.

Formfaktor
$$W_{a} = \frac{\Delta f_{a}}{f_{c}}  \s  W_{s} = \frac{\Delta f_{s}}{f_{c}}, \s F = \frac{W_{s}}{W_{a}}$$

The transformation back to band-pass:
$$H_{bp}(s) = H_{lp}(\bar{s})|_{\bar{s} = \frac{1}{W_{a}}\left(\frac{s+1}{s}\right)}$$


%% 
TODO: List low-pass
TODO: List high-pass 
TODO: List band-stop
%% 

---
#signalprocessing
