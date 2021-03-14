import tensorflow as tf

state=tf.Variable(0,name='counter')
# print(state.name)

one=tf.constant(1) #常量

new_value=tf.add(state,one)

update=tf.assign(state,new_value) #将new_value的值加载到state中

init=tf.initialize_all_variables() #初始化

with tf.Session() as sess:
    sess.run(init) #初始化变量
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))

