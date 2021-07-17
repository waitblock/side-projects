num_darts <- 1000
num_darts_in_circle <- 0

x <- runif(n=num_darts,min=-1,max=1)
y <- runif(n=num_darts,min=-1,max=1)

sum_squares<-x^2+y^2
indexes_darts_in_circle <- which(sum_squares<=1)
num_darts_in_circle <- length(indexes_darts_in_circle)

print(4 * num_darts_in_circle/num_darts)

for(i in 1:num_darts){
  plot(x[1:i],y[1:i], xlim=c(-1,1),ylim=c(-1,1))
  points(x[i],y[i],col="red")
  Sys.sleep(0.5)
}