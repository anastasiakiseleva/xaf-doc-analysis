---
uid: "403184"
title: 'Localize UI Elements'
owner: Eugenia Simonova
---
# Localize UI Elements

This lesson explains how to localize an XAF application. It describes how to translate UI elements into German and create a multi-language application.

> [!NOTE]
> For more information on localization, review the following topics:
> 
> * [How to: Localize an XAF Application](xref:402956)
> * [Localization Basics](xref:112595)

## Step-by-Step Instructions

1. [Add](https://learn.microsoft.com/en-us/nuget/consume-packages/install-use-packages-visual-studio) the following packages to the **MySolution.Blazor.Server** and **MySolution.Win** projects:

   | Project name                 | Package name               |
   |------------------------------|----------------------------|
   | **MySolution.Blazor.Server** | _DevExpress.ExpressApp.de_<br>_DevExpress.ExpressApp.Blazor.de_ |
   | **MySolution.Win**           | _DevExpress.ExpressApp.de_<br>_DevExpress.ExpressApp.Win.de_ |                           

   The packages are available only for the following languages: German (de), Spanish (es), and Japanese (ja). For other languages, use the [Localization Service](xref:16235) to download satellite assemblies. See the [Localize Standard XAF Modules and DevExpress Controls Used in an Application](xref:113301) topic for more information on how to use this service to localize XAF modules.
    
2. In the **MySolution.Blazor.Server** project, open the _appsettings.json_ file. Add the German language to the _DevExpress:ExpressApp:Languages_ section and enable the [runtime language switcher](xref:403027). You should always use the fully qualified language name that includes the country code (for example, `de-DE` instead of `de`):

    # [appsettings.json](#tab/tabid-csharp)

    ```JSON{5,6}
    { 
        // ... 
        "DevExpress": { 
            "ExpressApp": { 
                "Languages": "en-US;de-DE",
                "ShowLanguageSwitcher": true,  
                 // ...
            } 
        } 
    }  
    ```
    ***
 
    See the [Current Culture in XAF ASP.NET Core Blazor Applications](xref:402956#current-culture-in-xaf-aspnet-core-blazor-applications) help section for more information on how an XAF ASP.NET Core Blazor application determines the default language.

3. Open the _Model.DesignedDiffs.xafml_ file in the [Model Editor](xref:112582). Focus the _MySolution_ node and click **Languages Manager…** in the **Language** combo box on the [Model Editor Toolbar](xref:113327).

   ![Run language manager](~/images/blazor-tutorial-run-languages-manager.png)    

4. Add the target language in the invoked dialog and click **OK**. 
 
   ![The language manager](~/images/blazor-tutorial-languages-manager.png)

   Save the model changes but don't restart Visual Studio as the Languages Manager suggests. When you restart Visual Studio, the Model Editor loads the localized property value from the assemblies that you added previously and they become available at design time. For the purposes of this tutorial, these values aren't necessary.
 
5. In the Solution Explorer, right-click the _Model.DesignedDiffs.Localization.de-DE.xafml_ file and open its **Properties** window. Make sure that the **Build Action** field is set to **Embedded resource**.

6. Open the _Model.DesignedDiffs.xafml_ file in the [Model Editor](xref:112582). Select the newly added language in the **Language** combo box.

   ![|Select language|](~/images/tutorial_uic_lesson11_0_1115628.png)

7. The localization packages translate standard strings/messages used in XAF. You also need to translate the strings that are unique to your current application (such as object or property names). To do that, locate properties denoted by the "globe" glyph in all the nodes and child nodes and assign a German translation to them. For the purposes of this tutorial, translate the **Employees** navigation item to _Angestellte_:

   ![|Localize captions|](~/images/blazor-tutorial-localize-captions.png)

   >[!TIP]
   >Instead of going through each node to find strings that require translation one by one, use the [Localization Tool](xref:113297) to streamline your localization process. 
 
8. In the **MySolution.Win** project, open the _Model.xafml_ file in the [Model Editor](xref:112582) and navigate to the **MySolution** node. Set the **PreferredLanguage** property to `de-De` to display the localized strings in the UI when you run the Windows Forms application.

9. Run the application.

   In ASP.NET Core Blazor, you can switch the language in the application settings menu. To access the settings menu, click the gear icon in the upper right corner:

   ![|Language switcher in ASP.NET Core Blazor application settings|](~/images/blazor-tutorial-lang-switcher.png)

10. The application should display the German translation of the **Employees** navigation item.

    ASP.NET Core Blazor

    :   ![|Localized caption in the ASP.NET Core Blazor Navigation Control|](~/images/blazor-tutorial-localized-app.png)

    Windows Forms

    :   ![Localized caption in the Windows Forms Navigation Control](~/images/blazor-tutorial-localized-app-winforms.png)

## Next Lesson

[](xref:404201)
