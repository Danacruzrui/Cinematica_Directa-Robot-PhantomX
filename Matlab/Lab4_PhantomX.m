%                         Lab4_Cinematica_Directa-PhantomX -Pincher- ROS 


%Desarrollado por:   Daniel Cruz y Cristhian Pulido

syms q1 q2 q3 q4 ; 
tetha= [q1, q2, q3, q4]; d=[42,0,0,0];%  entre xi-1 y xi a lo largo de zi-1
alpha= [-pi/2, 0 , 0, 0];  a= [0, 104, 104 , 90 ];%entre zi-1 y zi a lo largo de xi.

L(1) = Link('revolute','alpha',alpha(1),'a',a(1),'d',d(1));
L(2) = Link('revolute','alpha',alpha(2),'a',a(2),'d',d(2),'offset', -pi/2);
L(3) = Link('revolute','alpha',alpha(3),'a',a(3),'d',d(3));
L(4) = Link('revolute','alpha',alpha(4),'a',a(4),'d',d(4));


figure
subplot(2,3,1)
PhantomX = SerialLink(L,'name','PhantomX');
PhantomX.plot([deg2rad(0) deg2rad(0)  deg2rad(0) deg2rad(0)],'notiles','noname'); % Pose #1 (HOME)
xlim([-200 300]);ylim([-200 300]);zlim([-50 400]); view([130 30]);

subplot(2,3,2)
PhantomX = SerialLink(L,'name','PhantomX');
PhantomX.plot([deg2rad(20) deg2rad(-20)  deg2rad(20) deg2rad(-20)],'notiles','noname'); % Pose #2 
xlim([-200 300]);ylim([-200 300]);zlim([-50 400]); view([130 30]);

subplot(2,3,3)
PhantomX = SerialLink(L,'name','PhantomX');
PhantomX.plot([deg2rad(-30) deg2rad(30)  deg2rad(-30) deg2rad(30)],'notiles','noname'); % Pose #3 
xlim([-200 300]);ylim([-200 300]);zlim([-50 400]); view([130 30]);

subplot(2,3,4)
PhantomX = SerialLink(L,'name','PhantomX');
PhantomX.plot([deg2rad(-90) deg2rad(15)  deg2rad(-55) deg2rad(17)],'notiles','noname'); % Pose #4
xlim([-200 300]);ylim([-200 300]);zlim([-50 400]); view([130 30]);

subplot(2,3,5)
PhantomX = SerialLink(L,'name','PhantomX');
PhantomX.plot([deg2rad(-90) deg2rad(45)  deg2rad(-55) deg2rad(45)],'notiles','noname'); % Pose #5