---
uid: DevExpress.ExpressApp.Win.SystemModule.SystemWindowsFormsModule.PrintingSettingsStorage
name: PrintingSettingsStorage
type: Property
summary: Specifies whether printing settings are saved separately for each [View](xref:112611).
syntax:
  content: |-
    [DefaultValue(PrintingSettingsStorage.Application)]
    public PrintingSettingsStorage PrintingSettingsStorage { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Win.SystemModule.PrintingSettingsStorage
    description: An value that specifies whether printing settings are saved separately for each View.
seealso:
- linkId: "113012"
- linkId: "113283"
---
When a user modifies print options in the **Page Setup** or **Preview** dialog, the options are saved in the [Application Model](xref:112580) and are applied to every View in the application.

Set the `PrintingSettingsStorage` property to `View` to save print model settings for each [View](xref:112611) separately.

# [SolutionName.Win\ApplicationBuilder.cs](#tab/tabid-cs)
 
```csharp
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication() {
        builder.AddBuildStep(application => {
            // Configure PrintingSettingsStorage
            var systemModule = application.Modules.FindModule<DevExpress.ExpressApp.Win.SystemModule.SystemWindowsFormsModule>();
            if (systemModule != null) {
                systemModule.PrintingSettingsStorage = DevExpress.ExpressApp.Win.SystemModule.PrintingSettingsStorage.View;
            }
            // ...
```
***