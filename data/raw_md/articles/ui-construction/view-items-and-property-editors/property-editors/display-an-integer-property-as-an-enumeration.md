---
uid: "113563"
seealso: 
- linkId: "403100"
title: 'Display an Integer Property as an Enumeration (WinForms)'
owner: Ekaterina Kiseleva
---
# Display an Integer Property as an Enumeration (WinForms)

This topic describes how to display a business class integer property as an enumeration, in case you do not wish to modify (or cannot modify) the source code of this class.

> [!NOTE]
> ASP.NET Core Blazor applications do not support displaying of a business class integer property as an enumeration.

Consider the following `SampleObject` business class.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[DefaultClassOptions]
public class SampleObject : BaseObject {
    public virtual string Name { get; set; }
    public virtual int IntegerProperty { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[DefaultClassOptions]
public class SampleObject : BaseObject {
    public SampleObject(Session session) : base(session) { }
    private string name;
    public string Name {
        get { return name; }
        set { SetPropertyValue(nameof(Name), ref name, value); }
    }
    private int integerProperty;
    public int IntegerProperty {
        get { return integerProperty; }
        set { SetPropertyValue(nameof(IntegerProperty), ref integerProperty, value); }
    }
}
```
***

Assume that this class is located in an external assembly, and you cannot modify its code. The task is to display enumeration values instead of integers (for example, `Value1` for zero, `Value2` for `1`, and so on). Follow these steps to learn how to solve this task:

1. Implement an enumeration whose values will be mapped to integer values.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	public enum SampleEnum { Value1, Value2, Value3}
	```
	***
2. Create a custom **MyEnumIntPropertyEditor** Property Editor by inheriting the `EnumIntPropertyEditor\<SampleEnum>` class in the [WinForms application project](xref:118045) (_MySolution.Win_). [!include[PublicEditor](~/templates/publiceditor111797.md)]
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.Editors;
	using DevExpress.ExpressApp.Model;
	using DevExpress.ExpressApp.Win.Editors;
	// ...
	[PropertyEditor(typeof(int), false)]
	public class MyEnumIntPropertyEditor : EnumIntPropertyEditor<SampleEnum> {
	    public MyEnumIntPropertyEditor(Type objectType, IModelMemberViewItem model)
	        : base(objectType, model) {  }
	}
	```
	***
3. Run the Model Editor for the WinForms project. Set the [IModelCommonMemberViewItem.PropertyEditorType](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType) property of the **BOModel** | **OwnMembers** | **IntegerProperty** node to **MyEnumIntPropertyEditor**.

The following image illustrates the results in a WinForms application:


![EnumIntPropertyEditor_Win](~/images/enumintpropertyeditor_win117318.png)
