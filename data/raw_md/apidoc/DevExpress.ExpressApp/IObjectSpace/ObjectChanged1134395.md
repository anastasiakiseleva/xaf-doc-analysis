---
uid: DevExpress.ExpressApp.IObjectSpace.ObjectChanged
name: ObjectChanged
type: Event
summary: Occurs when a persistent object is created, deleted or changed (when the objects' [INotifyPropertyChanged.PropertyChanged](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged) event occurs).
syntax:
  content: event EventHandler<ObjectChangedEventArgs> ObjectChanged
seealso:
- linkId: "2077"
- linkId: DevExpress.ExpressApp.Editors.PropertyEditor.ValueStored
---
You can handle this event in a custom [Controller](xref:112621) to execute business logic when an object is changed.

[!include[](~/templates/objectchanged_code_snippet.md)]

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to declare this event. It's declared within the **BaseObjectSpace class**. The **BaseObjectSpace.OnObjectChanged** method raises this event. So, you should only invoke the **OnObjectChanged** method in your **BaseObjectSpace.SetModified** method override.

> [!NOTE]
> [!include[EF_ObjectChanged_Note](~/templates/ef_objectchanged_note111120.md)]
