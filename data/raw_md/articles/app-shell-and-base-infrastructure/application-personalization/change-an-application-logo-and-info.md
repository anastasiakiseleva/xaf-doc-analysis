---
uid: "113156"
title: 'Change an Application Logo and About Information'
---
# Change an Application Logo and About Information

This topic describes how to change an application logo and description text. The following list details where these elements appear depending on the application platform.
* ASP.NET Core Blazor: the top-left corner of the application's main page.
  
  ![|XAF ASP.NET Core Blazor Logo Image, DevExpress|](~/images/LogoImage_Blazor.png)
  
* Windows Forms: the application's **About** window.
  
  ![XAF Windows Forms Logo Image, DevExpress](~/images/logoimage116232.png)

In Windows Forms applications, you can [use an embedded resource image](#use-a-custom-logo-image) as a logo.

> [!NOTE]
> In Windows Forms applications, you can use the [AboutInfoController.AboutInfoAction](xref:DevExpress.ExpressApp.Win.SystemModule.AboutInfoController.AboutInfoAction) Action to invoke the **About** window. It contains the [](xref:DevExpress.ExpressApp.SystemModule.AboutInfo) object's Detail View (`AboutInfo_DetailView`).
>
> ASP.NET Core Blazor applications display the @DevExpress.ExpressApp.SystemModule.AboutInfo.AboutInfoString property value on the Template.

## Specify Application Information

In the [Model Editor](xref:112582), you can use the following properties or the root **Application** node to specify application name, description, vendor, copyright, and version:

![XAF Model Editor Application Node Properties, DevExpress](~/images/aboutme117538.png)

## Use a Custom Logo Image

### In ASP.NET Core Blazor Applications

XAF adjusts the specified logo image according to the current theme and renders it as monochromatic (black and white) by default.

Depending on your application behavior or corporate style, you can use one of the following techniques:

#### Colorful Logo

To preserve the colors of your custom logo, specify the `background-image` attribute.

1. Add the image you want to use to the _MySolution.Blazor.Server\\wwwroot\\images_ folder.
2. Navigate to the _YourSolutionName.Blazor.Server\\wwwroot\\css\\site.css_ file and specify the image's name in the `header-logo` CSS class. 

   ```css{2}
   .header-logo {
       background-image: url(../images/CustomLogo.svg);
       width: 180px;
       height: 24px;
       /* ... */
       background-position: center;
       background-size: contain;
       background-repeat: no-repeat;
   }
   ```
   ![|Colorful Custom Logo Image, ASP.NET Core Blazor, DevExpress|](~/images/colorful-logo-xaf-blazor-devexpress.png)

####  Black and White Logo

If you do not want a colored custom logo and prefer that your current theme makes the logo image monochromatic (black and white), use the `mask` attribute.

Set the `background-color` property to `currentColor` to use the current color style. This applies to SVG images only.

1. Add the image you want to use to the _MySolution.Blazor.Server\\wwwroot\\images_ folder.
2. Navigate to the _YourSolutionName.Blazor.Server\\wwwroot\\css\\site.css_ file and specify the image's name in the `header-logo` CSS class. 

   ```css{2-3,7}
   .header-logo {
	   -webkit-mask: url('../images/CustomLogo.svg');
       mask: url('../images/CustomLogo.svg');
       width: 180px;
       height: 24px;
       /* ... */
       background-color: currentColor;
       -webkit-mask-position: center;
       mask-position: center;
       -webkit-mask-repeat: no-repeat;
       mask-repeat: no-repeat;
   }
   ```

   ![|Custom Logo Image, ASP.NET Core Blazor, DevExpress|](~/images/LogoImageBlazor.png)

### In Windows Forms Applications 

To use a custom logo, follow the steps below:
	
1. Save your custom logo to the _Images_ folder in the module project (for example, _MySolution.Module\Images\CustomLogo.png_).
		
2. In **Solution Explorer**, click the **Show All Files** toolbar button. In the **Images** sub-folder, right-click the image you added and choose **Include In Project**.
3. Switch to the **Properties** window. Set the **Build Action** option to **Embedded Resource**.
4. Rebuild the solution and invoke the [Model Editor](xref:112582). Focus the root **Application** node and click the [IModelApplication.Logo](xref:DevExpress.ExpressApp.Model.IModelApplication.Logo) property's ellipsis button. In the invoked **Image Picker** dialog, choose your logo.
	
	![|XAF Model Editor Image Picker, DevExpress|](~/images/logoimageme117290.png)
	
	If you enter the image name manually, omit the file extension.
	
	> [!NOTE]
	> In Windows Forms applications, the default logo is specified in the [user differences](xref:112580#application-model-layers) layer (individual user settings). To use the logo specified in the user differences, open the _Model.xafml_ file from the application project, navigate to the **Application** node, and delete the **Logo** property value.

To ensure changes to the logo in a Windows Forms application, run the application and invoke the **About** window.
	
![LogoImageWin](~/images/logoimagewin116233.png)
	
Refer to the [Application Personalization](xref:113445) topic for more information on the **About** window.
