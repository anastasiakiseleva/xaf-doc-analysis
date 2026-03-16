---
uid: DevExpress.ExpressApp.Frame.SaveModel
name: SaveModel()
type: Method
summary: Writes information about the [](xref:DevExpress.ExpressApp.Frame)'s [View](xref:112611) and [Template](xref:112609) to the [Application Model](xref:112580).
syntax:
  content: public void SaveModel()
seealso:
- linkId: DevExpress.ExpressApp.View.SaveModel
- linkId: DevExpress.ExpressApp.View.ModelSaving
---
This method writes the current settings of the [](xref:DevExpress.ExpressApp.Frame)'s [View](xref:112611) and [Template](xref:112609) to the corresponding [Application Model](xref:112580) nodes. For example, it saves layout settings in Detail Views and List Editor settings in List Views. The system calls this method automatically when a window closes.

You usually do not need to call this method. You can handle the [Frame.ViewModelSaving](xref:DevExpress.ExpressApp.Frame.ViewModelSaving) and [Frame.ViewModelSaving](xref:DevExpress.ExpressApp.Frame.TemplateModelSaving) events. The system raises these events when it synchronizes information on the frame's view and template.

## Example

[!include[save-app-state-example](~/templates/save-app-state-example.md)]