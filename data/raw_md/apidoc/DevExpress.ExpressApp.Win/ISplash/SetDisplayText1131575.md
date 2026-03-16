---
uid: DevExpress.ExpressApp.Win.ISplash.SetDisplayText(System.String)
name: SetDisplayText(String)
type: Method
summary: Sets the text to be displayed by the label located on the default splash screen form.
syntax:
  content: void SetDisplayText(string displayText)
  parameters:
  - id: displayText
    type: System.String
    description: A string value representing the text to be shown on the default splash screen form.
seealso: []
---
The splash screen form shown by a Windows Forms XAF application, by default, contains a label. This label has the "Loading…"  text assigned. You can set another text by using the **SetDisplayText** method of the object returned by the application's **SplashScreen** property.

# [C#](#tab/tabid-csharp)

```csharp
static class Program {
    static void Main() {
        //..
        MySolutionWindowsFormsApplication application = new MySolutionWindowsFormsApplication();
        try {
            application.SplashScreen.SetDisplayText("MyText");
            application.Setup();
            application.Start();
        }
        //...
    }
}
```
***

The **SetDisplayText** method must be called before the **Setup** method call. Otherwise, the splash screen with the default text will be shown.

When implementing a custom splash screen, you do not have to implement the **SetDisplayText** method:

# [C#](#tab/tabid-csharp)

```csharp
public class MySplash : ISplash {
    //...
    public void SetDisplayText(string displayText) {}
}
```
***

If your splash screen form contains a label, you can set the required text to it explicitely, without additional code.