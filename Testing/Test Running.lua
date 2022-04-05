inputs = {A, B, X, Y, Left, Right, Up, Down}
savestate.load("C:\Users\fynnm\Desktop\Projektarbeit\SNES\State\Savestate 1-1.State")
while true do
    joypad.set({Right = true, B=true}, 1)
    emu.frameadvance()
    joypad.set({B=false}, 1)
