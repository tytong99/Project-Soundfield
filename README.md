# Project soundfield: Acoustic-Array-Simulator-Project
><h2>Aim of this thing:</h2>
<p>
Simple, quick, intuitive, naive, easy-to-use soundfield simulation/visualisation/algorithm prototyping in-house python package for any acoustic array numerical with signal integration.
</p>
<p align="center">
  
  <img src="https://github.com/tytong99/Project-Soundfield/blob/main/img/beamformer_gain.PNG" width="350" title="numerical simulation of beamformer directivity">
</p>
<p align="center">
  Soundfield visualisation, beamformer directivity numerical simulation
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
>Style: Naive OPP (I'm a script kid and I'm arrogant about it) with no checks
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
If you think this project is a good idea, feel free to contribute and have a chat. My progress on building this project is typically extremely slow (I am recently drifting away from analytical solutions to numerical simulation).
</p>
