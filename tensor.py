class Tensor():
    def __init__(self, data, shape):
        self.data = data
        self.shape = shape
        self.tensor = ...

    def shape_data(self):
        # outputs an empty list if shape is an empty list
        if self.shape == []:
            return []
        # make sure data is int or float, and shape is a list of positive integers
        for s in self.shape:
            if type(s) != int or s<1:
                print('Shape needs to be a list of positive integers')
                return
        for d in self.data:
            if type(d) !=int and type(d) != float:
                print('Data needs to be a number (int or float)')
                return
        # calculates dimension of the tensor
        dim = 1
        for j in self.shape:
          dim = dim * j
        # stores data in data_list and modified according to specified dimensions
        data_list = self.data
        #if not enough data numbers, pad tensor w/ 0s
        if len(self.data) < dim:
          for i in range(dim - len(self.data)):
            data_list.append(0)
        #if too many data numbers, cut off after tensor fills up
        elif len(self.data) >= dim:
          del data_list[dim:]

        # slices the data list into groups specified by shape, starting with the last index
        # the loop repeats for each data point (excluding the first b/c dimension has already been accounted for)
        # updates the sliced list every iteration
        for j in range(1, len(self.shape)):
          data_list = ([data_list[x:x+self.shape[-1*j]] for x in range(0, len(data_list), self.shape[-1*j])])

        #prints the constructed tensor
        print(data_list)

# example 1
data0 =  [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
shape0 = [2, 3, 2]
tensor0 = Tensor(data0, shape0)
# example 1 output
Tensor.shape_data(tensor0)

# example 2
data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
shape1 = [5, 2]
tensor1 = Tensor(data1, shape1)
# example 2 output
Tensor.shape_data(tensor1)
