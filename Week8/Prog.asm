@0
D = A
@0
A = M
M = D
@0
M = M + 1
@1
D = M
@0
D = D + A
@13
M = D
@0
M = M - 1
A = M
D = M
@13
A = M
M = D
(LOOP_START)
@2
D = M
@0
A = D + A
D = M
@0
A = M
M = D
@0
M = M + 1
@1
D = M
@0
A = D + A
D = M
@0
A = M
M = D
@0
M = M + 1
@0
M = M - 1
A = M
D = M
@0
M = M - 1
A = M
M = M + D
@0
M = M + 1
@1
D = M
@0
D = D + A
@13
M = D
@0
M = M - 1
A = M
D = M
@13
A = M
M = D
@2
D = M
@0
A = D + A
D = M
@0
A = M
M = D
@0
M = M + 1
@1
D = A
@0
A = M
M = D
@0
M = M + 1
@0
M = M - 1
A = M
D = M
@0
M = M - 1
A = M
M = M - D
@0
M = M + 1
@2
D = M
@0
D = D + A
@13
M = D
@0
M = M - 1
A = M
D = M
@13
A = M
M = D
@2
D = M
@0
A = D + A
D = M
@0
A = M
M = D
@0
M = M + 1
@0
M=M-1
A=M
D=M
@LOOP_START
D;JNE
@1
D = M
@0
A = D + A
D = M
@0
A = M
M = D
@0
M = M + 1
