---
uid: "404211"
title: 'How to: Change View Display Mode from Tabbed MDI to Single Window (SDI)'
owner: Anastasiya Kisialeva
---
# How to: Change View Display Mode from Tabbed MDI to Single Window (SDI)

This article describes how to change the way a Windows Forms and ASP.NET Core Blazor application displays the invoked Views.

> [!NOTE]
> For the purposes of this article, you can use the **MainDemo** application installed as a part of the XAF package. The default location of the application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\\Components\XAF_.

The [Template Kit](xref:405447) creates an application with the Tabbed MDI powered by the @DevExpress.XtraBars.Docking2010.DocumentManager (Windows Forms) and @DevExpress.Blazor.DxTabs (ASP.NET Core Blazor), so the application displays every invoked View in a new tab.

> [!NOTE]
> A Tabbed MDI is a multiple document interface (MDI) UI metaphor found in many modern applications (including your favorite Web browser or Microsoft Outlook Web). It is a robust interface that maximizes document screen real estate, especially when you work with multiple documents, email messages, and so on.

ASP.NET Core Blazor
:   ![|XAF ASP.NET Core Blazor Tabbed View, DevExpress](~/images/how-to-chooose-blazor-ui-tabbed-view-devexpress.png)
Windows Forms
:   ![XAF Windows Forms Tabbed View, DevExpress](~/images/how-to-chooose-winforms-ui-tabbed-view.png)

The instructions below explain how to enable _Single Document (SDI)_ mode instead of Tabbed View mode in an application. In SDI mode, every time you invoke a View, it appears in a new window that replaces the previous one.

1. In the **Solution Explorer**, expand the _MainDemo.Blazor.Server_ (ASP.NET Core Blazor) or _MainDemo.Win_ (Windows Forms) project folder and double-click the _Model.xafml_ file to open it in the [Model Editor](xref:112582).

2. Navigate to the **Options** node. Here you can customize the appearance and behavior of the application's UI.

3. Focus the `UIType` property and choose the **SingleWindowSDI** option from the drop-down menu.

   ASP.NET Core Blazor
   :   ![|XAF ASP.NET Core Blazor UIType property of the Options node, DevExpress](~/images/how-to-chooose-blazor-ui-modelapp-devexpress.png)

   Windows Forms
   :   ![|XAF Windows Forms UIType property of the Options node, DevExpress](~/images/how-to-chooose-winforms-ui-modelapp.png)

4. Run the application and see the new View display mode in action.
	
   ASP.NET Core Blazor
   :   ![XAF ASP.NET Core Blazor SDI, DevExpress](~/images/how-to-chooose-blazor-ui-sdi-devexpress.gif)

   Windows Forms
   :   ![XAF Windows Forms SDI, DevExpress](~/images/how-to-chooose-winforms-ui-sdi.png.gif)
	
> [!TIP]
> To change the View display mode in code, specify the @DevExpress.ExpressApp.XafApplication.ShowViewStrategy property or override the `XafApplication.CreateShowViewStrategy` method (advanced). If you specify the View display mode in code, XAF ignores the @DevExpress.ExpressApp.UIType property value changes in the Model Editor.
