# DH-Parameters
See the [[Lecture 7 - DH Parameters and Forward Kinematics.pdf|slides]].

A standard for placing frames on a robot.
![[dh-parameter-table.png|center|250]]

Every joint can be describes as a combination of prismatic and revolute joints.

*Prismatic joint*: Pure translation in one axis
*Revolute joint*: Pure rotation in one axis

#### Variables
These values are derived for every link. $i$ denotes the link index.

$a_{i-1}$: Link length, shortest distance between two joint axis.
$\alpha_{i-1}$: Link twist, the angle between the axis around $a_{i-1}$.
$d_{i}$: Link offset
$\theta_{i}$: Joint angle, angle of connection to the next joint, around the joint axis.

>[!example]- Images
>![[Pasted image 20230621105223.png]]
>![[Pasted image 20230621105657.png]]

#### Placing Frames (Modified Craig)
- The **origin** of frame $\set{i}$ is located where $a_{i}$ intersects joint axis $i$.
- The **Z-axis** of frame $\set{i}$ is coincident with joint axis $i$.
- The **X-axis** of frame $\set{i}$ points along $a_{i}$ in the direction from joint $i$ to joint $i + 1$.
- The **Y-axis** of frame $\set{i}$ follows in order to form a right-handed coordinate system.

>[!example]- Image
>![[Pasted image 20230621110417.png]]

## Procedure
See [[Lecture 7 - DH Parameters and Forward Kinematics.pdf#page=29|slide]]:

1. Identify the joint axes and consider them as infinite lines
2. Identify the common perpendicular between them or the point of intersection
3. Assign the origins, Z-axes and X-axes of frames $\set i$ according to frame convention.
4. Assign the Y-axes of frames $\set i$ to yield right-handed co
5. Assign frame $\set 0$ and frame $\set N$ according to [[Lecture 7 - DH Parameters and Forward Kinematics.pdf#page=26|convention]].
6. For each pair of frames $\set i$ and $\set{i+1}$, identify the four DH parameters:

$\alpha_i$ - The **angle** from $\hat{Z}_i$ to $\hat{Z}_{i+1}$ measured about $\hat{X}_i$
$a_i$ - The **distance** from $\hat{Z}_i$ to $\hat{Z}_{i+1}$ measured along $\hat{X}_i$
$d_i$ - The **distance** from $\hat{X}_{i-1}$ to $\hat{X}_i$ measured along $\hat{Z}_i$
$d_i$ - The **angle** from $\hat{X}_{i-1}$ to $\hat{X}_i$ measured about $\hat{Z}_i$

>[!example]- Assigning DH Parameters
>![[Lecture 7 - DH Parameters and Forward Kinematics.pdf#page=33]]

---
#kinematics 
