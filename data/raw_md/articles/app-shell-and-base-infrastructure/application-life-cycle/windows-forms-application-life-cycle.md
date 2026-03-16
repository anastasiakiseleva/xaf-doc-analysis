---
uid: "113115"
seealso: []
title: Windows Forms Application Life Cycle
owner: Ekaterina Kiseleva
---
# Windows Forms Application Life Cycle

The table in this topic details the steps performed while an XAF Windows Forms application is running.

| Stage | Description |
|---|---|
| **Application is created** | See [Windows Forms Application Creation and Initialization](xref:113119). |
| **Splash screen is invoked** | The [ISplash.Start](xref:DevExpress.ExpressApp.Win.ISplash.Start) method of the @DevExpress.ExpressApp.Win.ISplash object assigned to the [WinApplication.SplashScreen](xref:DevExpress.ExpressApp.Win.WinApplication.SplashScreen) method is called. This method shows the splash screen form.<br/><br/>See also: <xref:112680>. |
| **An end-user is authenticated** | See [User Authentication using a Logon Window in Windows Forms Applications](xref:113117) and [User Authentication Without a Logon Window in Windows Forms Applications](xref:113124).<br/><br/>See also: <xref:404264>. |
| **Start-up Popup Window Show Actions are executed** | A collection of Popup Window Show Actions is populated by the Actions that are registered as start-up Actions in modules used by the application. For instance, the [ChangePasswordOnLogon](xref:112649) represents a start-up Action. A pop-up window is displayed for each Action after an end-user has executed or canceled the previous Action.<br/><br/>To register an Action as a start-up, override the `GetStartupActions` method in your module class. Return a list of Popup Window Show Actions in this method. |
| **Main window is shown** | The application object asks its Show View Strategy (see [](xref:DevExpress.ExpressApp.ShowViewStrategyBase)) to show a main window. Since, at this moment, the Show View Strategy is requested for the first time, it has not yet been created. So, an instance of the `ShowInMultipleWindowsStrategy` class is created, and then its `ShowStartupWindow` method is called. (See [Show the Main Window in Windows Forms Applications](xref:113118).) |
| **Splash screen is closed** | A splash screen is closed by the [ISplash.Stop](xref:DevExpress.ExpressApp.Win.ISplash.Stop) method. |
| **Main window is displayed until a user closes it** | A user can close the main window by executing the **Exit** or **LogOff** Action. The **Exit** Action closes the application. The **LogOff** Action closes the main form and re-invokes the logon form. |