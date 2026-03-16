---
uid: "113445"
title: Application Icon, Logo & About Info
---
# Application Icon, Logo & About Info

## Application Logo and Info

XAF-powered Blazor applications display this information at the top-left and bottom-left corners of the main page. To customize a logo image for an Blazor application, specify the image name in the **header-logo** CSS class. 

![|XAF Logo and About Image ASP.NET Core Blazor, DevExpress](~/images/LogoImage_Blazor.png)

XAF-powered WinForms applications display an application logo and supplementary application information within an **About** window. You can specify info texts in the [Model Editor](xref:112582)'s **Application** root node. This node also allows you to change a logo image in WinForms applications.

![XAF Logo Image Windows Forms, DevExpress](~/images/logoimage116232.png)

For more information, refer to the following help topic: [Change an Application Logo and Info](xref:113156).

## Blazor Application Icon
To change the application icon that is displayed in browser tabs, replace the _MySolution.Blazor.Server\\wwwroot\\favicon.ico_ file with a custom image. This approach applies to all ASP.NET Core applications.

![BlazorIcon](~/images/BlazorIcon.png)

## WinForms Application Icon

XAF specifies a WinForms application icon in the **Icon** property within the **Application** page of the **Project Designer**. This approach is common for Windows Forms applications (see [How to: Specify an Application Icon](https://learn.microsoft.com/en-us/visualstudio/ide/how-to-specify-an-application-icon-visual-basic-csharp)). The icon is displayed in the compiled application at the top-left corner of the form, in the Windows Explorer, and the Windows taskbar. The default icon (_ExpressApp.ico_) is in the WinForms application project folder.

![IconWin](~/images/iconwin117536.png)

**See also:** [Application Page, Project Designer (C#)](https://learn.microsoft.com/en-us/visualstudio/ide/reference/application-page-project-designer-csharp)

## Blazor Application Splash Screen

XAF-powered Blazor applications display the following Splash Screen on startup:

![Blazor Splash Screen](~/images/BlazorSplashScreen.png)

You can customize the default Splash Screen's caption and image in the _MySolution.Blazor.Server\\Pages\\\_Host.cshtml_ file. If you want to use a custom image, add it to the _MySolution.Blazor.Server\\wwwroot\\images_ folder. 

# [CSHTML](#tab/tabid-cshtml)

```CSHTML
<!-- ... -->
<html lang="en">
<body>
    <!-- ... -->
    <component type="typeof(SplashScreen)" 
                   render-mode="Static" 
                   param-Caption='"My Blazor application"' 
                   param-ImagePath='"images/CustomSplashScreenImage.svg"' />
    <!-- ... -->
</body>
</html>
```

***

The following image shows the customized Splash Screen:

![Custom ASP.NET Core Blazor Splash Screen](~/images/CustomBlazorSplashScreen.png)

If you want to display a custom Splash Screen instead of the default screen, follow the steps below:
1. Add a new Razor component to the ASP.NET Core Blazor application project. You can customize the built-in **SplashScreenComponent** or create your own. Note that the built-in Splash Screen uses the parameters specified in the _\_Host.cshtml_ file. The following code snippet shows how to customize **SplashScreenComponent** and access the **param-ImagePath** parameter:

    # [Razor](#tab/tabid-razor)
    
    ```Razor
    @using DevExpress.ExpressApp.Blazor.Components
    <SplashScreenComponent>
        <LoadingIndicator>
            <img class="rounded bg-primary text-white p-3" src="@ImagePath" />
        </LoadingIndicator>
    </SplashScreenComponent>
    @code {
        [CascadingParameter(Name = "ImagePath")] 
        protected string ImagePath { get; set; }
    }

    ```
    
    ***

2. In the _MySolution.Blazor.Server\\Pages\\\_Host.cshtml_ file, set the Splash Screen's **param-ContentType** parameter to the type of the newly created component:

    # [CSHTML](#tab/tabid-cshtml)

    ```CSHTML{9}
    <!-- ... -->
    <html lang="en">
    <body>
        <!-- ... -->
        <component type="typeof(SplashScreen)" 
                    render-mode="Static" 
                    param-Caption='"My ASP.NET Core Blazor application"' 
                    param-ImagePath='"images/CustomSplashScreenImage.svg"'
                    param-ContentType="typeof(MySolution.Blazor.Server.Component)" />
        <!-- ... -->
    </body>
    </html>
    ```

    ***

![Custom ASP.NET Core Blazor Splash Screen Component](~/images/CustomBlazorSplashScreenComponent.png)


The example below customizes Splash Screen properties dynamically in code:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Components;
using DevExpress.ExpressApp.Blazor.Services;
using Microsoft.AspNetCore.Components;
//..
public class CustomSplashScreen : SplashScreen {
    [Inject] private IXafApplicationProvider XafApplicationProvider { get; set; }
    private string caption;
    protected override void OnInitialized() {
        base.OnInitialized();
        XafApplication Application = XafApplicationProvider.GetApplication();
        caption = Application.Model.Company;
    }
    protected override void OnParametersSet() {
        base.OnParametersSet();
        Caption = caption;
    }
}
```
After that, place this descendant in the _MySolution.Blazor.Server\Pages\_Host.cshtml_ file:
```CSHTML{5}
<!-- ... -->
<html lang="en">
<body>
    <!-- ... -->
    <component type="typeof(CustomSplashScreen)" 
                render-mode="Static" 
                param-Caption='"My ASP.NET Core Blazor application"' 
                param-ImagePath='"images/CustomSplashScreenImage.svg"'
           />
    <!-- ... -->
</body>
</html>
```

You can also show the loading panel/indicator in XAF Blazor applications. For more information on possible approaches, refer to the following topic: [](xref:404738).

## WinForms Application Splash Screen


XAF-powered WinForms applications display the following [Splash Screen](xref:112680) on startup:

![splashform splashscreen](~/images/SplashForm01_SplashScreen.png)

Applications with the [Security System](xref:113366) also display the [Overlay Form](xref:112680) over the [Logon Form](xref:113151).

![splashform overlay form](~/images/SplashForm02_OverlayForm.png)

You can customize the startup behavior as described in the following help topics: 
* [Splash Forms](xref:112680)
* @DevExpress.ExpressApp.ModuleBase.GetStartupActions