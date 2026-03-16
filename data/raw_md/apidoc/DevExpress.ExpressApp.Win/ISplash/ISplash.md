---
uid: DevExpress.ExpressApp.Win.ISplash
name: ISplash
type: Interface
summary: Declares members implemented by a splash screen which is displayed when a Windows Forms application starts.
syntax:
  content: public interface ISplash
seealso:
- linkId: DevExpress.ExpressApp.Win.ISplash._members
  altText: ISplash Members
---
When a Windows Forms application starts, a splash screen is displayed. Usually, it shows basic information on the starting application, its logo and/or version, while the application is being initialized (see [Windows Forms Application Creation and Initialization](xref:113119)). In XAF, the splash screen represents an object that implements the **ISplash** interface. This interface exposes the **Start** and **Stop** methods. The **Start** method is invoked by the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method before initializing the application's service objects. In the **Start** method, a splash form must be shown. This form must be closed by the **Stop** method, which is called when the main form is invoked.

In XAF applications, a default splash screen form is shown automatically. This form contains a label, whose text is set to "Loading…". You can change this text by calling the [ISplash.SetDisplayText](xref:DevExpress.ExpressApp.Win.ISplash.SetDisplayText(System.String)) method before the application's **Setup** method is called. To access the splash screen currently set to the application, use the [WinApplication.SplashScreen](xref:DevExpress.ExpressApp.Win.WinApplication.SplashScreen) property.

To replace the default splash screen with a custom one, assign an instance of your Splash class that implements the **ISplash** interface to the application's **SplashScreen** property:

# [C#](#tab/tabid-csharp)

```csharp
static class Program {
    static void Main() {
        //..
        MySolutionWindowsFormsApplication application = new MySolutionWindowsFormsApplication();
        try {
            application.SplashScreen = new MySplash();
            application.Setup();
            application.Start();
        }
        //...
    }
}
```
***

Note that you should perform the assignment before the **Setup** method call. Otherwise, a form of the default splash screen will be shown.

To see an example of a custom splash screen, refer to the [Splash Forms](xref:112680) topic.