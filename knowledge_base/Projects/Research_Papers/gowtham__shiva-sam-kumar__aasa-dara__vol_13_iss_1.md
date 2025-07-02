Design and Optimization of Lug Bracket Assembly

G. GOWTHAM*,1, G. SHIVA SAM KUMAR1, AASA DARA1

*Corresponding author
1Department of Aeronautical Engineering,
Veltech Rangarajan Dr. Sagunthala R&D Institute of Science & Technology,
Chennai, India
gowthamg@veltech.edu.in*, shivasamkumar1@gmail.com, aasad3698@gmail.com

DOI: 10.13111/2066-8201.2021.13.1.6

Received: 17 June 2020/ Accepted: 10 January 2021/ Published: March 2021
Copyright © 2021. Published by INCAS. This is an “open access” article under the CC BY-NC-ND
license (http://creativecommons.org/licenses/by-nc-nd/4.0/)

Abstract: An aircraft is an advanced mechanical structure made by man which has been dominating
the skies from the early 19th centuries. It has been used for transportation of cargo/ passengers from
one place to another in a shorter period of time. Advances in aeronautics lead to the development of
fighter aircrafts with exciting and dominating characteristics. A fighter aircraft is to be designed in
such a way that it can withstand heavy loadings on the wing due to its high manoeuvrability. A fighter
aircraft  is  designed  to  be  marginally  unstable,  which  makes  control  easier  and  better  during
manoeuvrability at high speeds, but in this state there is a heavy fluctuating load acting on the wing.
The wing is connected to the fuselage using wing fuselage lug attachment bracket. Since the wing is a
cantilever structure, the load acting on the wing is concentrated on the hinge (lug bracket assembly).
In this paper, a lug bracket is designed according to the standard design procedure and is validated
using Finite Element Methods to ensure the static loading capability and stress concentrations in lug
bracket. The validated model has been optimized using Altair Optistruct. The optimized model has been
validated under static loading condition for the stress concentration and displacement and is compared
with initial model in order to study and understand its behaviour under various conditions.

Key Words: Fighter aircraft, Finite element method, optimization, stress concentration, static loading
condition, validation

1. INTRODUCTION

Aircraft are the most popular transportation in recent times as they reduce travel time. They
are used to transport goods and civilians and are also used for military purposes. Their size,
shape and configurations differ depending on the requirements. It is rather a challenging task
to design a fighter aircraft, as it dominates the sky through its high speed and must withstand
many loads and difficulties due to manoeuvrability and be able to accomplish the task without
affecting any structure [1], [5]. The structure of an aircraft is mainly divided into three basic
parts such as fuselage, wing and empennage.

Wing and fuselage are considered important parts of an aircraft. As wings are subjected
to different loads, they are supposed to be rigidly fixed to the fuselage. This attachment is done
by a series of pinned lugs between the wing side of wing box and the fuselage through which
the bending moment and shear loads are transferred from wing to fuselage thus, aircraft wing-
fuselage lug attachment bracket is the one on which the maximum loads act [3], [9]. When the
lug undergoes a catastrophic failure, it may lead to the separation of the entire aircraft structure.

INCAS BULLETIN, Volume 13, Issue 1/ 2021, pp. 55 – 67        (P) ISSN 2066-8201, (E) ISSN 2247-4528

G. GOWTHAM, G. SHIVA SAM KUMAR, AASA DARA

56

One end of the lug is attached to the fuselage and the other end is attached to the I-spar of the
wing. Hence, the entire structure of the wing acts as a cantilever beam with the lug bracket
attached/ fixed to the fuselage which transfers the load to the fuselage. The connection between
the wing and the fuselage of the aircraft occurs with four lugs of which, two at the front spars
and two at the rear spars.

The entire load is evenly distributed among these spars and is transferred through the lug
pin. In order to increase the lifetime of this lug bracket and to reduce the frequent inspection
cost,  Finite  Element  Analysis (FEA) is performed  to validate the stress  concentrations and
for  easy
optimize
manufacturability with minimized constraints [2], [4].

lug-bracket  assembly  (Topology  and  shape  optimisation)

the

2. OBJECTIVE

The objectives of this project are as follows:
➢  To design a new model according to the standard design procedure and the reference lug

models.

➢  To conduct linear static analysis of the bracket to obtain:

•  Maximum von-Mises stress
•  Maximum shear stress
•  Other necessary contours

➢  To perform modal analysis of the lug attachment bracket to analyse the behaviour of the

lug under the natural frequency.

➢  To interpret the results of linear static and conduct optimization according to topology and
shape to reduce or constrain the values of displacement stress and frequency values.
➢  To derive a final model which has less volume fraction, weight, minimum compliance and
reduced stress and displacement contours which can be replaced with the existing model.

3. DESIGN TERMINOLOGY

Here we re-create a new model for lug-bracket assembly. To do that, first we have to decide
how the new lug model should look like. The pre-existing lug models from references [16],
[20] are obtained and studied.

The lug has to be designed with the dimensions and geometry that will help the lug bracket
to withstand the heavy loading conditions derived in the previous section. The dimension for
the lug bracket is achieved through the standard design procedure which is as follows. The
material we have used is Steel AISI-4340.

The load applied on the lug-bracket assembly is 90584.62 N (P). [12], [16], [20] for light

weight fighter aircraft.

Here, the design is based on yield stress i.e., 𝜎𝑦𝑡 = 1550 N/mm2 (which is the yield stress

of the material used). Considering,

𝜎𝑦𝑡 =

𝑃
𝐴

(1)

Substituting the yield stress 𝜎𝑦𝑡 and load P in the above equation, we get the diameter of

the pin hole 𝐷𝑝.

1550 =

90584.62
𝜋𝑟2

(2)

INCAS BULLETIN, Volume 13, Issue 1/ 2021

57

Design and Optimization of Lug Bracket Assembly

r = 24.795 mm

D = 49.59 mm

Bearing stress is calculated as

𝜎𝑏𝑒𝑎𝑟𝑖𝑛𝑔 =

𝑃
𝐴𝑏𝑒𝑎𝑟𝑖𝑛𝑔

 =

𝑃
𝐷×𝑡

Bearing strength = 0.5 ×  𝜎𝑦𝑡 = 0.5 × 1550 = 775

N
mm2

But,

𝜎𝑏𝑒𝑎𝑟𝑖𝑛𝑔 =

𝑃
𝐷×𝑡

(3)

(4)

(5)

(6)

Substituting load P, Diameter D and obtained bearing stress, we get the thickness t, of our lug.

775 =

90584.62
𝑟×𝑡

t = 80mm (approx.)

Height of the lug hole = 3.5×Di = 181.35 mm

(7)

(8)

(9)

A  3-D  model  of lug  bracket  with  the  above  dimensions is modelled  using  CATIA-V5
(Designing tool) and drafted down to visualize the model in different projections as shown in
fig. 1.

Fig. 1 – Orthographic projections

4. MATERIAL SELECTION

In Aeronautical industry, strength, rigidity and weight are the most important properties in
material selection. In many situations trials and errors can be very expensive and for a good
project design, material selection is very important. The material properties to be considered
for the selection of material for structural applications are:
➢  Yield stress
➢  Ultimate Tensile stress
➢  Temperature limits
➢  Fatigue resistance
➢  Corrosion resistance

INCAS BULLETIN, Volume 13, Issue 1/ 2021

G. GOWTHAM, G. SHIVA SAM KUMAR, AASA DARA

58

➢  Fracture toughness
➢  Crack growth resistance
➢  Ductility

In  this  paper  AISI-4340  is  used to model the lug  bracket.  The  steel alloy is  examined
according to the material properties considered for selection in structural applications [22],
[21]. The material properties are tabulated below in Table 1.

Table 1. – Material properties

PROPERTIES
Young’s Modulus, E

Poison’s Ratio, 𝜇
Ultimate Tensile Strength,
UTS
Yield Stress, 𝜎𝑦

Density, 𝜌

STEEL AISI-4340

𝑁
𝑚𝑚2

211000
0.3

2200

1550

7.85

𝑁
𝑚𝑚2
𝑁
𝑚𝑚2
𝑔
𝑐𝑚3

5. FINITE ELEMENT ANALYSIS

Finite  Element  Method  (FEM)  is  widely  used  for  solving  engineering  problems  and
mathematical  models.  It  is  a  particular  numerical  method  used  to  solve  partial  differential
equations consisting of two or three variables. It is increasingly becoming the primary tool for
designers and analysts [1], [3]. The new model for lug-bracket assembly of fighter light-weight
aircraft is recreated.

The  structural  behaviour  of  the  component  is  identified  and  studied  using  a  technique
called Finite Element Analysis (FEA). The analytical solution for the lug bracket can be solved
using  FEA solutions  such as  Ansys,  Nastran-Patran, Ansa,  Hyperworks.  In  this  project  for
linear static analysis and optimization we use Hyperworks [5], [7], [8]. Altair Hyperworks is
the  most  comprehensive  simulation  platform  offering  the  best  set  of  solvers  to  design  and
optimize to high performance increasing the efficiency of the product.

6. DISCRETIZATION

Meshing also known as Discretization is a process of dividing an element into n-number of
smaller elements. The accuracy in the analytical solution of the component highly depends on
the quality of the mesh in the component [13], [14]. Meshing can be classified into two types
based on one quality.
➢  Coarse mesh = medium sized elements
➢  Fine mesh = very small and fine sized elements
The time taken for solving the problem depends on the size of the elements, if the element size
is smaller the solving time is longer [16], [17], [18]. Meshing based on the element can be
classified as 1-D, 2-D and 3-D meshing.

In this paper we are using 3-D element for meshing the lug bracket. 3-D elements are
generally  used  when  all  the  dimensions  are  comparable.  There  are  various  types  of  3-D
elements such as Tetra, Penta, Hexa or Brick and Pyramid. 3-D elements are generally used to
mesh solid mould components such as Gear box, Engine box, Crank shaft, etc [15]. A 3-D
tetra element is used to mesh the lug bracket. Both the R-Tria and Tria elements are set as the

INCAS BULLETIN, Volume 13, Issue 1/ 2021

59

Design and Optimization of Lug Bracket Assembly

base elements in the 3-D tetra mesh [19], [20]. The lug bracket had been divided into two parts,
one is the design space and other is the non-design space.

The nodes across the bolt holes had been joined through 16 rigid body element (RBE2).
A total of 37,588 elements are used in the non-design space and 89,752 elements are used in
the design space part of the lug-bracket. The RBE2 elements are constrained to 6 degrees of
freedom to transfer all the loads equally to pin holes, as shown in fig. 2.

Fig. 2 – 3-D Tetra mesh

7. LOADS AND BOUNDARY CONDITIONS

The pin holes of the lug joint has been constrained to 6 degrees of freedom (yellow) and a total
force of 5661.538 N [12], [16] is applied to each lug hole, since the end flange is to be attached
to the I-spar; the lift load is represented in positive Y direction in the interconnected nodes of
lug holes as shown in figs. (3-4).

Fig. 3 –Fixed to 6 degrees of freedom

Fig. 4 – Loads distributed equally

8. RESULTS AND INTERPRETATION

After setting the loads and boundary conditions for the re-created lug-bracket it is ready for
analysis. PARAM, SCREEN and OUTPUT Cards are used for the Analytical solution. The
results for the shear stress, von-Mises stress, von-Mises strain and displacement are obtained.
The contours for the results are obtained as shown in figs. (5-8).

INCAS BULLETIN, Volume 13, Issue 1/ 2021

G. GOWTHAM, G. SHIVA SAM KUMAR, AASA DARA

60

Fig. 5 – Shear stress

Fig. 6 – Von-Mises stress

Fig. 7 – Displacement

Fig. 8 – Von-Mises strain

The  results  for  shear-stress,  von-Mises  stress,  von-Mises  strain  and  displacement  are
tabulated  in  Table  2  below  and  interpreted.  From  the  contour  plots  it  is  identified  that  the
maximum von-Mises stress is located in the fillet regions. This region may be the starting point
of the crack and the volume of the lug bracket is too high [19]. The displacement values are
higher at the flange tips which leads to a heavy vibration in the wings. To reduce the volume,
the material orientation has to be identified and optimized [11].

S. NO
1.
2.
3.
4.
5.
6.

Table 2. – Results

CONTOURS
Maximum Von-Mises stress
Maximum Shear stress
Maximum Von-Mises strain
Displacement
Weight
Volume

VALUE
183.791 MPa
95.022 MPa
0.002
4.358 mm
0.851 kg
1.15 𝑚𝑚3

9. OPTIMIZATION AND TYPES

Optimization in general is defined as the method of finding a best and satisfying solution from
all the feasible solutions.

Structural  optimization  is  a  discipline  or  branch  dealing  with  optimal  design  of  load-

carrying mechanical structures [3].

INCAS BULLETIN, Volume 13, Issue 1/ 2021

61

Design and Optimization of Lug Bracket Assembly

Given  a  pre-defined  design  domain  (in  two  or  three  dimensions),  external  loads  and
material to be used are defined. The problem is to define an optimal structure to carry these
loads. The objective of the optimization problem may be stated as reduced weight, constrained
displacement and modal frequency values. The optimization can be classified into:
➢  Topology optimization,
➢  Shape optimization,
➢  Size optimization,
➢  Topography optimization.

10. TOPOLOGY OPTIMIZATION

Topology optimization is a mathematical method that optimizes the material layout within a
given design space, for a given set of loads, boundary conditions and constraints with a goal
of maximizing the performance of the system.

Topology  optimization  provides  a  perfect  orientation  for  the  material  placement  and
shows us the places from which the material can be removed without affecting the stiffness
and rigidity of the structure and reduces the volume of structure [2], [5].

In  this  section  the  lug-bracket  is  optimized  to  optimal  shape  using  the  topology
optimization. Optimal shape for the lug bracket is obtained by removing the material from the
area due to which there will be no effect in stiffness of the structure. The constraints for the
topology optimization is defined in Table 3.

Objective

Response

Constraints

Table 3. – Topology Optimization constraints

Minimize volume
Minimize weighted compliance
Von-Mises stress < 180 MPa
Weighted compliance
Nodal displacement constrained in Y-axis
Displacement < 1.5 mm
Shear stress <95 MPa

The procedure for the optimization is defined using a formula

D = Design variable
R = Responses
D = De constraint
O = Objective

The four general steps to be followed for any optimization is given as follows.

➢  The  design  space  is  defined  i.e. the place  from  where  the material is to  be removed is

identified and selected.

➢  Responses are nothing but the definition of the objective and constraints.
➢  De-constraint  panels  offer  the  space  to  define  the  lower  and  upper  bound  for  the

constraints.

➢  Objective  panel  defines  the  final  objective  of  the  optimization  like  minimum  volume,

maximum frequency, minimum and maximum Von-Mises stress, etc.
The  topology  optimization  following  these  steps  is  performed.  The  stress  and  nodal

displacements are constrained as mentioned in the table.

The element density is obtained from the results of topology optimization as shown in

Fig. 9.

INCAS BULLETIN, Volume 13, Issue 1/ 2021

G. GOWTHAM, G. SHIVA SAM KUMAR, AASA DARA

62

Fig. 9 – Material orientation

Fig. 10 – Von-Mises stress after 75th iteration

Fig. 11 – Displacement after 75th iteration

INCAS BULLETIN, Volume 13, Issue 1/ 2021

63

Design and Optimization of Lug Bracket Assembly

Fig. 12 – Shear stress after 75th iteration

The  change  in  von-Mises  stress,  von-Mises  strain  and  displacement  after  the  iteration
(optimization) is shown in Fig. (10-12). The results of optimization are tabulated in Table 4.

Table 4. – Topology Optimization results

Iteration  Von-Mises

stress (Mpa)

Von-Mises
strain

Displacement
(mm)

Max shear
stress (Mpa)

Weight (kg)

0th

75th

183.791

167.45

0.02

0.02

4.358

1.685

95.022

84.499

0.851

0.651

Volume
(𝒎𝒎𝟑)
1.15

0.908

11. SHAPE OPTIMIZATION

In  a  structural  shape  optimization  problem  the  aim  is  to  improve  the  performance  of  the
structure by modifying its boundaries.

This can be numerically achieved by minimizing an objective function subjected to certain

constraints [17].

The  typical  problem  of  shape  optimization  is  to  find  the  shape  which  is  optimal  and
minimize certain cost functions while satisfying the given constraints. In the previous section
the lug-bracket was optimized using the topology optimization. In the Fig. 12 it is seen that
the critical stress areas are at the fillets [19].

So  in  this  section  the  fillets  in  the  inner  region  of  the  lug  bracket  are  optimized.  The

constraints for the shape optimization are as in Table 5.

Table 5. – Shape Optimization constraints

Objective
Minimize stress (maximum von-Mises stress)
No constraints
Constraints
Design variable  Grids move normal to the surface

The procedure for shape optimization is the same as for the topology optimization, but
some  changes  are  done  in  the  design  space  and  design  variable  because  the  mode  of
optimization is different.

In this section we will learn about the procedure followed for the free-shape optimization

in Optistruct.

INCAS BULLETIN, Volume 13, Issue 1/ 2021

G. GOWTHAM, G. SHIVA SAM KUMAR, AASA DARA

64

➢  The Hypermesh solver is opened and the Optistruct user profile is loaded.
➢  The solver setup for lug bracket is installed and the property collector, load collector, and

the material collector are verified.

➢  A new component and property collectors are created for the elements in the fillet region.
➢  The elements in the fillet regions are transferred to the newly created component through
the organizing panel and property (same as for lug-bracket) is designed to the component.

➢  The fillet regions are separated as identical components as in Fig. 14.
➢  Now the optimization panel is used to setup the optimization.
➢  Free shape optimization is selected from the optimization panel.
➢  The grid points in outer face of the new component as shown in Fig. 14 are selected as the

deign space.

➢  The response of static stress is selected from the response panel.
➢  The objective of the optimization is stated as to minimize the maximum von-Mises stress.
➢  The file is saved and Optistruct solver is selected for optimization.

The  shape  optimization  problem  is  solved and  the  result  is obtained.  The  result  in  the

shape change for the fillet areas as shown in Fig. (15-16).

The  objective  of  the  problem,  namely  minimizing  the  maximum  von-Mises  stress  has

been achieved.

The maximum von-Mises stress for the lug bracket after shape optimization is achieved

as 118.151 MPa as shown in Fig. 17.

Fig. 13 – Design space

Fig. 14 – Divided into 3 individual components

Fig. 15 – Shape change in upper fillet

Fig. 16 – Shape change in bottom fillet

INCAS BULLETIN, Volume 13, Issue 1/ 2021

65

Design and Optimization of Lug Bracket Assembly

Fig. 17 – Minimized max von-Mises stress

12. RESULTS

In the previous section we saw the results of the finite element analysis and optimization of
the models for the lug bracket.

In this section we will compare the results of the models for the lug bracket and validate
a final design for the lug bracket. The comparison of the results of the lug bracket models is
tabulated in Table 6.

Table 6. – Comparison of results

S. No  Models

Weight
(kg)

Volume
(𝑚𝑚3)

Von-Mises
stress (MPa)

1.

2.

Recreated

0.851

1.15

183.791

Optimized

0.651

0.908

167.45

Von-
Mises
strain

0.02

0.02

Displacement
(mm)

4.358

1.685

Shear
stress
(MPa)

95.022

84.499

The most important factor for evaluating the service life of the lug bracket design can be
defined as the load-bearing capacity of the component or the intensity of the component to
withstand the stress.

From  the  tabular  column  we  can  see  that  the  volume  and  von-Mises  stress  for  the

optimized lug bracket is very low compared to the other two models.

The stress concentration of the optimized model of the lug bracket is seen in the fillet
regions; thus the fillets of the lug bracket are also optimized using the free size optimization
by  increasing  the  inner  radius  of  the  fillet,  which  is  shown  in  the  previous  section.  The
optimized model for the lug bracket has a minimized compliance factor which states that the
model has a higher stiffness factor.

The volume of the optimized model is compared with the other two models and it is found
that it has a minimum volume of 0.908mm3. The von-Mises stress and a shear stress value for
the optimized model are constrained to 167.45 MPa and 84.499 MPa, respectively which states
that the optimized model has a higher capacity to load for a longer period of time than the
initial model. The displacement value of the optimized model is achieved as 1.685 mm which
states that the model is highly rigid and has a high tensile strength.

INCAS BULLETIN, Volume 13, Issue 1/ 2021

G. GOWTHAM, G. SHIVA SAM KUMAR, AASA DARA

66

13. CONCLUSIONS

The Lug-Bracket assembly is used to establish  contact between the wing and fuselage of the
aircraft and this is why it is said to be the most critical and complex load- bearing structure,
has a high degree of safety factor  and is manufactured with intense care and it also has a a
higher resilience. From this research paper we can conclude that the optimization technique
can be used to reduce the weight of the Lug bracket assembly and to minimize the maximum
stress acting on the fillet regions of the Lug bracket. The optimized lug bracket model has a
low compliance factor which means the weight of the bracket is reduced but the stiffness of
the bracket is not compromised , which means the lug bracket assembly has a higher strength
to weight ratio and higher load bearing capacity. Thus, the optimized model of lug bracket is
highly efficient and can withstand longer working hours in heavy loading conditions; also, the
light weight of the bracket makes it suitable for easy and fast manufacturing.

REFERENCES

[1]  A.  Chinnamahammad  Bhasha,  K.  Balamurugan,  Fracture  Analysis  of  Fuselage  wing  joint  developed  by

aerodynamic structural materials, Materials Today: Proceedings, 1 September 2020.

[2]  J.  Zhu,  H.  Zhou,  C.  Wang,  L.  Zhou,  S.  Yuan,  W.  Zhang,  A  Review  of  topology  optimization  for  additive

manufacturing : Status and Challenges, Chinese Journal of Aeronautics, 13 October 2020.

[3] L. Song, T. Gao, L. Tang, X. Du, J. Zhu, Y. Lin, G. Shi, H. Liu, G. Zhou, W. Zhang, An all-movable rudder
designed by thermo-elastic topology optimization and manufactured by additive manufacturing, Computers
& Structures, Volume 243, 24 October 2020.

[4] C. Wang, X. Qian, Simultaneous optimization of build orientation and topology for additive manufacturing,

Additive Manufacturing, Volume 34, 11 May 2020.

[5] M. Nirish, R. Rajendra, Suitability of metal additive manufacturing processes for part topology optimization –
A comparative study, Materials Today:Proceedings, Volume 27, Part 2, Pages 1601-1607, 12 April 2020.
[6] C. M. Sample, V. K. Champagne, A. T. Nardi, D. A. Lados, Factors governing static properties and fatigue,
fatigue crack growth and fracture mechanisms in cold spray alloys and coatings/repairs: A review, Additive
Manufacturing, Volume 36, 12 June 2020.

[7]  Z.  Wang,  A.  S.  J.  Suiker,  H.  Hofmeyer,  T.  Hooff,  B.  Blocken,  Coupled  aerostructural  shape  and  topology
optimization of horizontal-axis wind turbine rotor blades, Energy Conversion and Management, Volume
212, 15 May 2020.

[8] S. Singamneni, L. V. Yifan, A. Hewitt, R. Chalk, W. Thomas, D. Jordison, Additive Manufacturing for the
Aircrfat  Industry:  A  Review,  Journal  of  Aeronautics  &  Aerospace  Engineering,  Volume  8,  Issue  1,  18
February 2019.

[9] S. M. Fijul Kabir, K. Mathur, A.-F. M. Seyam, A critical review on 3D printed continuous fiber-reinforced
composites:  History,  mechanism,  materials  and  properties,  Composite  Structures,  Volume  232,  19
September 2019.

[10] N. Shyamsunder, R. Suresh, U. Bhaskar, Design and Analysis of Landing Gear Lug Attachment Bracket for
Small  Transport  Aircraft,  International  Journal  of  Mechanical  Engineering  and  Technology  (IJMET),
Volume 9, Issue 3, March 2018.

[12] M. Khan, M. Rehman Khan, D. Smitha, Design and Analysis on Aircraft Wing to Fuselage Lug Attachment,
IOSR  Journal  of  Engineering,  Volume  1,  4th  International  Conference  Emerging  Trends  in  Mechanical
Science (ICEMS-2018).

[13] K. V. Prashant Reddy, I. M. Mirzana, A. Koti Reddy, Application of Additive Manufacturing technology to
an Aerospace component for better trade-off’s, Materials Today:Proceedings, Volume 5, Issue 2, Part 1,
Pages 3895-3902, 24 March 2018.

[14] C. Oberg, T. Shams, N.ader Asnafi, Additive Manufacturing and Business Models:Current Knowledge and

Missing Perspectives, Technology Innovation Management Review, June 2018.

[15]  Y.-C.  Wang, T.  Chen,  Y.-L.an  Yeh,  Advanced  3D printing  technologies  for  the  aircraft  industry:  A  fuzzy
systematic  approach  for  assessing  the  critical  factors,  The  International  Journal  of  Advanced
Manufacturing Technology, Volume 105, 05 April 2018.

[16] C. Shashikumar, N. Nagesh, Ganesh, Design and Analysis of Wing fuselage attachment bracket for fighter

aircraft, IJERGS, Volume 4, Issue 1, 2016.

INCAS BULLETIN, Volume 13, Issue 1/ 2021

67

Design and Optimization of Lug Bracket Assembly

[17]  B.  K.  Venkatesha,  K.  P.  Prashanth  and  T.  Deepak  Kumar,  Investigation  of  Fatigue  Crack  Growth  rate  in
Fuselage of Large Transport Aircraft using FEA Approach, Global Journal of Researches in Engineering,
Volume 14, Issue 1, Online ISSN:2249-4596 & Print ISSN:0975-5861, 2014.

[18] F. Hurlimann, R. Kelm, M. Dugas, G. Kress, Investigation of local load introduction methods in aircraft pre-
design, Aerospace Science and Technology, Volume 21, Issue 1, Pages 31-40, September 2012.

[19] S. K. Bhaumik, M. Sujata, M. A. Venkataswamy, Fatigue failure of aircraft components, Engineering Failure

Analysis, Volume 15, Issue 6, Pages 675-694, September 2008.

[20] O. Gencoz, U. G. Goranson and R. R. Merrill, Application of finite element analysis techniques for predicting
crack propagation in lugs, International Journal of Fatigue, Volume 2, Issue 3, Pages 121-129, Boeing
Commercial Airplane Company, Seattle, Washington, 98124, USA, July 1980.

INCAS BULLETIN, Volume 13, Issue 1/ 2021

