---
uid: DevExpress.ExpressApp.XafApplication.SetFormattingCulture(System.String)
name: SetFormattingCulture(String)
type: Method
summary: 'Sets the specified formatting culture for the XAF WinForms application. To localize and change formatting culture for the XAF ASP.NET Core Blazor applications, refer to the following topics: <xref:402956> and @DevExpress.ExpressApp.Blazor.Services.IXafCultureInfoService.'
syntax:
  content: public void SetFormattingCulture(string formattingCultureName)
  parameters:
  - id: formattingCultureName
    type: System.String
    description: The name of the formatting culture that must be used in the application.
seealso: []
---
An XAF application uses the formatting culture that is set in the current user's operating system or passed by the Internet browser (see [Culture-Specific Formatting](xref:113299)). You can set another formatting culture during the application's runtime. For this purpose, use the `SetFormattingCulture` method. Internally, this method changes the [Thread.CurrentCulture](https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread.currentculture#System_Threading_Thread_CurrentCulture) value. The simple example of using this method is provided in the [Culture-Specific Formatting](xref:113299). The more complex example is detailed below.

### Example

This example demonstrates how to add the `ChooseLanguage` and `ChooseFormattingCulture` Actions that allow end-uses to switch between predefined languages and formatting cultures. Perform the following steps:

1. Add a new Window Controller.
2. Invoke the Controller's Designer. Set the Controller's [WindowController.TargetWindowType](xref:DevExpress.ExpressApp.WindowController.TargetWindowType) property to `Main`.
3. Drag the `SingleChoiceAction` item from the Toolbox' **DX: XAF Actions** page to the Controller's Designer area. Set the Action's `Name` and `ID` properties (here, `ChooseLanguage`), the `Caption` property (here, `Choose Language`) and the [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property (here, `Tools`).
4. Drag and drop one more `SingleChoiceAction` item. Specify its properties correspondingly. Here, the `Name` and `ID` properties are set to `ChooseFormattingCulture`, and the `Caption` property is set to `Choose Formatting Culture`.
5. Subscribe to the Controller's [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event. In the event handler, populate the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection of the Controller's Actions with the required items (see the code).
6. Subscribe to the [SingleChoiceAction.Execute](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.Execute) event of the Controller's Actions. In the event handlers, call the [XafApplication.SetLanguage](xref:DevExpress.ExpressApp.XafApplication.SetLanguage(System.String)) and [XafApplication.SetFormattingCulture](xref:DevExpress.ExpressApp.XafApplication.SetFormattingCulture(System.String)) methods, respectively, passing the currently selected Action Item (see the code).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using System.Globalization;
//...
public partial class ChangeLanguageController : WindowController {
   public ChangeLanguageController() {
      InitializeComponent();
   }
   private string defaultCulture;
   private string defaultFormattingCulture;
   private void ChangeLanguageController_Activated(object sender, EventArgs e) {
      GetDefaultCulture      
      ChooseLanguage.Items.Add(new ChoiceActionItem(string.Format("Default ({0})", 
         defaultCulture), defaultCulture));
      ChooseLanguage.Items.Add(new ChoiceActionItem("German (de)", "de"));
      ChooseFormattingCulture.Items.Add(new ChoiceActionItem(string.Format(
         "Default ({0})", defaultFormattingCulture), defaultFormattingCulture));
      ChooseFormattingCulture.Items.Add(new ChoiceActionItem("German (de)", "de"));
   }
   private void GetDefaultCulture() {
      defaultCulture = CultureInfo.InvariantCulture.TwoLetterISOLanguageName;
      defaultFormattingCulture = CultureInfo.CurrentCulture.TwoLetterISOLanguageName;
   }
   private void ChooseLanguage_Execute(
      object sender, SingleChoiceActionExecuteEventArgs e) {
      Application.SetLanguage(e.SelectedChoiceActionItem.Data as string);
   }
   private void ChooseFormattingCulture_Execute(
   object sender, SingleChoiceActionExecuteEventArgs e) {
      Application.SetFormattingCulture(e.SelectedChoiceActionItem.Data as string);
   }
}
```
***