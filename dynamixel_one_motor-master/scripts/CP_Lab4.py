import math
import rospy
from std_srvs.srv import Empty
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from pynput.keyboard import Key, Listener, KeyCode  # keyboard input


def callback(data):
    rospy.loginfo(data.position)

def listener():
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)
    #rospy.spin()

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
#(-0.2914559245109558, 2.229382038116455, -2.56685733795166, -1.3550143241882324, 0.34258854389190674)
#(-0.3, 2.2 , -2.5 , -1.3, 0.3)
#(-0.29656916856765747, 2.1424567699432373, -2.4185729026794434, -1.324334740638733, 0.34258854389190674)

    # Print de comandos
    welcome = """\n 
                   ~~~~~~~ Lab. 4 - Cinematica Directa - Phantom X - ROS ~~~~~~~

Desarrollado por Daniel Cruz y Cristhian Pulido

Para ubicar el Robot en la posición deseada presione la tecla indicada seguida por Enter

            1:  Posición Home   (0, 0, 0, 0, 0.)
            2:  Posición 2     (-20, 20, -20, 20, 0.)
            3:  Posición 3     (30,-30, 30, -30, 0.)
            4:  Posición 4     (-90, 15, -55, 17, 0.)
            5:  Posición 5     (-90, 45, -55, 45, 10)

            9:  Posición x     Guardado
            0:  Activar retroalimentación de posición
                  """
    rospy.loginfo(welcome)
    while not rospy.is_shutdown():
       
        
        key= input()
        i=0
        
        if key == '1':
            
            state = JointTrajectory()
            state.header.stamp = rospy.Time.now()
            state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]
                
            point = JointTrajectoryPoint()

            ## 1. >>  0, 0, 0, 0, 0.
            point.positions = [math.radians(0), math.radians(0), math.radians(0), math.radians(0), math.radians(0)]  # 1
            
            point.time_from_start = rospy.Duration(0.5)
            state.points.append(point)
            pub.publish(state)            
            print('Posición 1: HOME')
            rospy.sleep(1)
    
        if key == '2':
   
            state = JointTrajectory()
            state.header.stamp = rospy.Time.now()
            state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]               
            point = JointTrajectoryPoint()
            ## 2. >>  -20, 20, -20, 20, 0.
            point.positions = [math.radians(-20), math.radians(-20),math.radians(-20), math.radians(20), math.radians(20)]  # 2
            
            point.time_from_start = rospy.Duration(0.5)
            state.points.append(point)
            pub.publish(state)
            print('Posición 2: -20, 20, -20, 20, 0.')
            rospy.sleep(1)
                        
        if key == '3':

            state = JointTrajectory()
            state.header.stamp = rospy.Time.now()
            state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]              
            point = JointTrajectoryPoint()

            ## 3. >>  30,-30, 30, -30, 0.
            point.positions = [math.radians(30), math.radians(-30), math.radians(30), math.radians(-30), math.radians(0)]  # 3
            
            point.time_from_start = rospy.Duration(0.5)
            state.points.append(point)
            pub.publish(state)
            print('Posición 2: 30,-30, 30, -30, 0.')
            rospy.sleep(1)

        if key == '4':

            state = JointTrajectory()
            state.header.stamp = rospy.Time.now()
            state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]                
            point = JointTrajectoryPoint()
             ## 4. >> -90, 15, -55, 17, 0.
            point.positions = [math.radians(-90), math.radians(15), math.radians(-55), math.radians(17), math.radians(0)]  # 4
            
            point.time_from_start = rospy.Duration(0.5)
            state.points.append(point)
            pub.publish(state)
            print('Posición 2: -90, 15, -55, 17, 0')
            rospy.sleep(1)

        if key == '5':

            state = JointTrajectory()
            state.header.stamp = rospy.Time.now()
            state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]
                
            point = JointTrajectoryPoint()

            ## 5. >> -90, 45, -55, 45, 10
            point.positions = [math.radians(-90), math.radians(45), math.radians(-55), math.radians(45), math.radians(10)]  # 5
            
            point.time_from_start = rospy.Duration(0.5)
            state.points.append(point)
            pub.publish(state)
            print('Posición 2: -90, 45, -55, 45, 10')
            rospy.sleep(1)

        if key == '9':

            state = JointTrajectory()
            state.header.stamp = rospy.Time.now()
            state.joint_names = ["joint_1", "joint_2","joint_3", "joint_4", "tool"]
                
            point = JointTrajectoryPoint()

            ## 5. >> Guardado
            point.positions = [-0.3, 2.2 , -2.5 , -1.3, 0.3]  # 5
            
            point.time_from_start = rospy.Duration(0.5)
            state.points.append(point)
            pub.publish(state)
            print('Posición X: Guardado')
            rospy.sleep(1)
        if key == '0':
           listener()

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass
