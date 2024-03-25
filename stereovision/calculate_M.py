# solving for M in the following equation
# ||    depth = M * (1/disparity)   ||
# for N data points coeff is Nx2 matrix with values 
# 1/disparity, 1
# and depth is Nx1 matrix with depth values
ret, sol = cv2.solve(coeff,z,flags=cv2.DECOMP_QR)