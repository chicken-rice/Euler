if __name__ == '__main__':
    side_len = 20
    vertex_num = side_len + 1

    route_data = [[0 for j in range(vertex_num)] for i in range(vertex_num)]
    route_data[0][0] = 1
    

    for i in range(vertex_num):
        for j in range(vertex_num):
            if i-1 >= 0:
                route_data[i][j] += route_data[i-1][j]
            if j-1 >= 0:
                route_data[i][j] += route_data[i][j-1]


    print route_data[vertex_num-1][vertex_num-1]
