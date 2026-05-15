---
uid: "113012"
seealso:
- linkId: "113283"
title: Print Data in WinForms Projects
---
# Print Data in WinForms Projects

The XAF printing system uses the [XtraPrinting](xref:2403) library to print and preview XAF [Views](xref:112611). The printing system contains the @DevExpress.ExpressApp.Win.SystemModule.PrintingController [View Controller](xref:112621) that is activated for Detail Views and List Views. 

Print Actions are displayed in the **File** main menu, in the context menu, and the **PrintPreview** Action is also available in nested List Views.

![Print Actions](~/images/xaf-printing-print-actions.png)

The printing system implements the following Actions:

Page Setup…
:   Invokes the **Page Setup** window where users can set up page printing options. This Action is enabled only for root Views.
	
	![Page Setup dialog](~/images/xaf-printing-page-setup.png)

Print Preview…
:   Shows how the current View will be printed. Users can make changes in the prepared page before printing. For instance, add color, margins, header, and footer.

	![Print Preview Dialog](~/images/xaf-printing-print-preview.png)
Print…
:   Invokes the **Print** dialog where users can set up printing options and print the prepared page. This Action is enabled only for root Views.
	
	![Print Dialog](~/images/xaf-printing-print-dialog.png)

## Print Custom List Editor

The [XtraPrinting](xref:2403) library enables printing for controls that implement the @DevExpress.XtraPrinting.IPrintable interface. XAF default Detail Views and List Views implement this interface and provide printing capabilities to users out of the box. 

If you use a custom List Editor to display List Views and want its data to be printable, implement the @DevExpress.ExpressApp.SystemModule.IExportable interface in the List Editor and the @DevExpress.XtraPrinting.IPrintable interface in the control it uses. 

Refer to the following help topic for additional information: <xref:3245>.

## Print Settings Storage

When a user modifies print options in the **Page Setup** or **Preview** dialog, the options are saved in the [Application Model](xref:112580) and are applied to every View in the application.

Set the @DevExpress.ExpressApp.Win.SystemModule.SystemWindowsFormsModule.PrintingSettingsStorage property to `View` to save print model settings for each [View](xref:112611) separately.

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