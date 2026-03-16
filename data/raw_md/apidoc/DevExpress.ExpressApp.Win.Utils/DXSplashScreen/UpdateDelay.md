---
uid: DevExpress.ExpressApp.Win.Utils.DXSplashScreen.UpdateDelay
name: UpdateDelay
type: Property
summary: Defines how often a [splash form](xref:112680) retrieves and displays status messages. Only [Splash Screens](xref:10823) and [Wait Forms](xref:10824) can show status messages.
syntax:
  content: public int UpdateDelay { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: Time between status message updates, in milliseconds.
seealso:
- linkId: "112680"
- linkId: DevExpress.ExpressApp.Win.Utils.DXSplashScreen.DefaultUpdateDelay
- linkId: DevExpress.ExpressApp.Win.Utils.DXSplashScreen.SetDisplayText(System.String)
- linkId: DevExpress.ExpressApp.Win.Utils.DXSplashScreen.UpdateSplash(System.String,System.String,System.Object[])
---
[Splash Screens](xref:10823) and [Wait Forms](xref:10824) retrieve and display information about current events as these events happen, when @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.DefaultUpdateDelay is set to zero. If you set the **UpdateDelay** property to a value other than zero, Splash Screens and Wait Forms retrieve and display information about current events at the specified intervals.

The  Splash Screen below is showing the _Starting…_ status message.

  ![splashformsplashscreen](~/images/SplashForm01_SplashScreen.png)
  
The following Wait Form is displaying the _Loading…_ status message.

  ![splashformwaitform](~/images/SplashForm03_WaitForm.png)