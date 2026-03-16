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
    description: A [](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingSettingsStorage) enumeration value specifying whether printing settings are saved separately for each View.
seealso:
- linkId: "113012"
---
The options specified in the "Page Setup" dialog and the 'Header and Footer' options, which are set in the Preview dialog, are saved automatically. The [](xref:DevExpress.ExpressApp.Win.SystemModule.IModelPrintingSettings) are added to the [Application Model](xref:112580), and filled with values each time printing setting are changed via the **PageSetup** or **PrintPreview** [Actions](xref:112622) for a [View](xref:112611). These options can be saved separately for each View, or they can be saved to the [](xref:DevExpress.ExpressApp.Model.IModelOptions), to affect all the Views in an application. By default, the options set for a View affect all the Views. You can change this behavior via the application project designer:

![PrintingSettingsStorage](~/images/printingsettingsstorage116313.png)