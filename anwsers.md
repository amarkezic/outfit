1. In PySide GUI framework, how and what component would you use if you wanted to customize/extend the rendering of an item in the ListView in a way that it would also display a custom icon on the far right side? (Example in an image below - Ps icon on the right)
    * I would use a combination of QPixmap and QLabel. QPixmap maps any image to QLabel.
    * Then i would create a custom widget where i could control the layout and place the image on the right side.
    * Then i would set the list item to the custom widhet with setItemWidget(listItem, widget).
2. Imagine you have an asset manager tool, similar to the one you built the GUI for in task 1. Let’s say you’re displaying a list of PSD (photoshop) files, each sized 3GB or more. The files are located on a remote server and your internet connection is relatively slow. How would you go about displaying the thumbnails for all those files without taking the program ages to load the thumbnails?

    * I would need to implement a function on the server side that compresses the image to a much smaller size. In python that can be done throught the PIL library (thumbnail function)

3. You have a list of N numbers. You must print out the number that is a duplicate in a list. If there are more duplicates in the list, just print out the first one, order doesn’t matter. How would you solve this problem? What data structure would you use and what algorithm?

    * I would use a for loop and a set data structure. I would insert 1 item by one item in the set when i can't insert the item in the set it means that i've found a duplicate and i print it out.

4. What is an object oriented approach in programming and how could you use it in the example of the GUI application you had to develop in task 1?
   
   * Object oriented programming is a concept where you program which objects which contains data and atributes, For exmaple a student could be an object (attributes: name, age, height, school) and i could be a specific instance of that object (Aljaz, 23, ...). For example i could wrap the QtlistWidget in a object with attributes TaskList(string listName, array tasks, string buttonName) {}

5. How do you calculate the normal at a given point on a 3d surface?

    *  If we have a vetor r(u,v) where u and v represent a point on that 3d surface, we can take the partials of r with respect to u and v meaning r_u and r_v. This new vector create a plane that is perpenticular to the 3d surface. Now if we take the cross product of those two vectors we get a new vector that is a **normal vector**. if we then devide this vector by its magnitude we get a **unit normal vector**. The formula is n(u,v) = (r_u x r_v)/(|r_u * r_v|)

6. Explain in general how a 2d texture is applied on a 3d surface. Which properties of the surface determine how the texture is applied. 

    * Textures are applied by mapping the 3d mesh of the model onto a 2d plane called the UV map. This a 2d representation of a 3d model.

7. Define what a 3d texture is and how it differs from a 2d texture.  Explain why a 3d texture could possibly slide on  the surface instead of sticking to it.  List what can be done to stick the texture to the surface.

    * a 2d texture has only two axises (u and v) and is like a sheet of paper, where as a 3d texture has 3 axies (u,v and w) so its like a stack of 2d sheets. They are mostly used for volumetric effects (fire, smoke.

8. Let’s say you have two cameras: camera1 and camera2. If P1 is the coordinate of a point in camera1 space,  describe the operations needed to transform P1 into camera2 space.

    * Divide the two camera spaces by a plane and then translate each point in the frist space through that plain by using vectors that have the same magnitude and direction but a different rotation.


