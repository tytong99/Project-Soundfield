# Project soundfield: Acoustic-Array-Simulator-Project
><h2>Aim of this thing:</h2>
>Simple, quick, intuitive, naive, easy-to-use soundfield simulation/visualisation/algorithm prototyping in-house python package for any acoustic array.
<p align="center">
![image](https://github.com/tytong99/Project-Soundfield/blob/main/img/focused_rectangle.PNG)![image](https://github.com/tytong99/Project-Soundfield/blob/main/img/beamformer_gain.PNG)
</p>
<p align="center">
Visualisation of focused acoustic array soundfield and numerical simulation of beamformer directivity
</p>

><h2>Generalised simulation procedure:</h2>
>
>**1.**
>
>Define source geometry
>
>Define source signal
>
>Define source filter/filterbank
>
>Define radiation pattern
>
>**2.**
>
>**If(want to see soundfield):**
>
>>Define soundfield grid
>>
>>sound transmission from source to soundfield
>>
>>compute soundfield
>
>**If(want to see receiver array performance):**
>>Define recipant geometry
>>
>>**If(direct transmission between transceivers):**
>>
>>>>sound transmission from source
>>
>>**If(receiver targets soundfield):**
>>
>>>>soundfield (Huygen-Fresnel) to receiver
>>>>
>>>>compute raw received signal
>>>>
>>>>receiver filter/filterbank
>>>>
>>>>compute receiver results
>>>>
>**3.**
>
>Physical quantity calibration
>
>**4.**
>
>Visualisation
>


>Datatype to process: Numpy ndarrays pretending to be matrices
>
>Style: Naive OPP (script kid) with no checks
>


><h2>Physical principles:</h2>
>
>Green function: in other word, impulse response & linear
>
>Rayleigh integral: add-things-up, normal people call this matrix multiplication nowadays
>
>Kirchoff-Helmholtz integral: one of those that, just, make, sense (but someone formulated it w/ integration, you've done calc I get it)
>
>Huygen-Fresnel principle: an excellent explanation to wave phenomena in the 1600s, and yet again it's called matrix multiplication now
>
>Sommerfield radiation condition: we talk farfield here
>
>Dirichlet boundary condition: simple point to point simulation, point doesn't move


<p>
If you think this project is a good idea, feel free to contribute and have a chat. My progress on building this project is typically extremely slow.
</p>
