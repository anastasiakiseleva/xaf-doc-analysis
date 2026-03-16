---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelActionBlazor.AdaptivePriority
name: AdaptivePriority
type: Property
summary: Specifies the Action's priority with regards to the adaptive and responsive layout used in the new web UI. Actions with a lower **AdaptivePriority** value remain visible when the browser window shrinks, while Actions with a higher priority become hidden.
syntax:
  content: |-
    [DefaultValue(1000)]
    int AdaptivePriority { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value that specifies the Action's priority with regards to the adaptive and responsive layout.
seealso: []
---
You can change the **AdaptivePriority** value in the [Model Editor](xref:112582). To invoke it, open the _MySolution\Blazor.Server\Model.xafml_ file.

![IModelActionWeb.AdaptivePriority_ModelEditor](~/images/imodelactionweb.adaptivepriority_modeleditor120588.png)

users can access Hidden Actions via the "..." button.

![IModelActionWeb.AdaptivePriority ](~/images/imodelactionweb.adaptivepriority120587.png)