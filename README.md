# Project soundfield: Acoustic-Array-Simulator-Project
>Aim of this thing:
>>Simple, quick, intuitive, easy-to-use soundfield simulation/visualisation/algorithm prototyping in-house python package for any acoustic array.


>Generalised simulation procedure:
>
>1.
>
>Define source geometry
>
>Define source signal
>
>Define source filter/filterbank
>
>Define radiation pattern
>
>2.
>
>If(want to see soundfield):
>
>>Define soundfield grid
>>
>>sound transmission from source to soundfield
>>
>>compute soundfield
>
>If(want to see receiver array performance):
>>Define recipant geometry
>>
>>If(direct transmission between transceivers):
>>
>>>>sound transmission from source
>>
>>If(receiver targets soundfield):
>>
>>>>soundfield (Huygen-Fresnel) to receiver
>>>>
>>>>compute raw received signal
>>>>
>>>>receiver filter/filterbank
>>>>
>>>>compute receiver results
>>>>
>3.
>
>Physical quantity calibration
>
>4.
>
>Visualisation
>


>Datatype to process: Numpy ndarrays pretending to be matrices
>
>Style: OPP (script kid)
>


>Physical principles:
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


