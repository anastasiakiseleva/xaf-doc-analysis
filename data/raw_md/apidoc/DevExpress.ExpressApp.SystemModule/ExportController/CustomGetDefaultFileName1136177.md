---
uid: DevExpress.ExpressApp.SystemModule.ExportController.CustomGetDefaultFileName
name: CustomGetDefaultFileName
type: Event
summary: Occurs when executing the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction). Allows you to customize the default name of the file to which data is exported.
syntax:
  content: public event EventHandler<CustomGetDefaultFileNameEventArgs> CustomGetDefaultFileName
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ExportController.CustomExport
---
By default, a file name is generated from the caption of the List View from which data is currently exported. Handle this event to provide a custom file name. To get or set the file name to be used by ExportCotnroller, use the event handler's [CustomGetDefaultFileNameEventArgs.FileName](xref:DevExpress.ExpressApp.SystemModule.CustomGetDefaultFileNameEventArgs.FileName) parameter.

Refer to the [How to: Customize the Export Action Behavior](xref:113287) topic, to see an example of handling this event.