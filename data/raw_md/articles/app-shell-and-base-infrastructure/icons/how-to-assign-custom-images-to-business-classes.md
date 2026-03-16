---
uid: "404209"
title: 'How to: Assign Custom Images to Business Classes'
owner: Anastasiya Kisialeva
---
# How to: Assign Custom Images to Business Classes

This article describes how to associate a business class with a custom image. This image appears next to the corresponding item in the Navigation control.

> [!NOTE]
> For the purposes of this article, you can use the **MainDemo** application installed as a part of the XAF package. The default location of the application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\\Components\XAF_.

The instructions below explain how to associate a custom image with the `Employee` class.

1. Create the _Images_ folder in the application module. Save the image below to this folder in PNG format and name it _Employee_:

   ![Custom image for Employee class](~/images/Employee.png)

   The file name should follow image name guidelines. Refer to the following article for additional information: [](xref:112792#image-file-names).

2. In the **Solution Explorer**, select the [MainDemo.Module](xref:118045) project and click the **Show All Files** toolbar button.

3. Select the image in the _Images_ subfolder, right-click the selection, and choose the **Include In Project** option. This image is now included in the project compilation.
	
	![Include custom image in the project](~/images/how-to-assign-custom-image-include-in-project.png)
	
4. In the **Solution Explorer**, right-click the image again and select the **Properties** option. Set the **Build Action** option to **Embedded Resource**.
	
	![Employee image properties](~/images/how-to-assign-custom-image-properties.png)

5. Invoke the [Model Editor](xref:112582). Navigate to the **BOModel** | **MainDemo.Module.BusinessObjects** | **Employee** node and set its `ImageName` property to `Employee`.
	
	![Employee node properties](~/images/how-to-assign-custom-image-imagename-property.png)
	
	> [!NOTE]
	> * When you select the `ImageName` property, an ellipsis button appears to the right of the property value. Click this button to invoke the **Image Picker** dialog and browse all available images.
	> * You can use the [](xref:DevExpress.Persistent.Base.ImageNameAttribute) to specify the image in code.

6. _Optional._ In the WinForms project of the **MainDemo** application, the Navigation control does not display images. To display the images, open the Application Model of the WinForms application project, navigate to the **NavigationItems** node, and set the `ShowImages` property to `True`.

   ![WinForms Model Application NavigationItems node](~/images/how-to-assign-custom-image-winform-modelapp.png)

7. Run the application. The **Employee** navigation item now displays the custom image:

   ASP.NET Core Blazor Application
	
   :   ![Employee with custom image - ASP.NET Core Blazor](~/images/how-to-assign-custom-image-result-blazor.png)
	
   WinForms Application
	
   :   ![Employee with custom image - WinForms](~/images/how-to-assign-custom-image-result-winforms.png)
