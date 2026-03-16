---
uid: "113052"
seealso: []
title: Ways to Build Criteria
owner: Ekaterina Kiseleva
seealso:
- linkId: "404016"
---
# Ways to Build Criteria

This topic demonstrates options for creating criteria when you use any of the [filtering techniques](xref:112998) in an XAF application.

## A Criteria as a CriteriaOperator Object
When you are required to set a criteria as a [](xref:DevExpress.Data.Filtering.CriteriaOperator) object, you have the following options:

* Use [Criteria Operators](xref:2129) provided by XPO. There are several XPO criteria operators that you can use to build the required criteria. The following code demonstrates how to build a simple criteria using the BinaryOperator:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.Data.Filtering;
	//...
	// The criteria that represents a logical expression (City <> "Chicago") 
	// is represented by the BinaryOperator and two operands.
	CriteriaOperator criteria = new BinaryOperator(
	    new OperandProperty("City"), new OperandValue("Chicago"),
	    BinaryOperatorType.NotEqual);
	```
	
	***
* Use the [CriteriaOperator.Parse](xref:DevExpress.Data.Filtering.CriteriaOperator.Parse*) method. You can represent criteria as a human-readable string and parse it using the static **CriteriaOperator.Parse** method. 
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.Data.Filtering;
	//...
	//The criteria that represents a logical expression (City <> "Chicago") is represented by a string.
	CriteriaOperator criteria = CriteriaOperator.Parse("City != 'Chicago'");
	```
	
	***
	
	To learn the syntax used in the **CriteriaOperator.Parse** method, refer to the [Criteria Language Syntax](xref:4928) help topic.

For details on how to build criteria using XPO techniques, refer to the following links:

* [Creating Criteria](xref:2036#creating-criteria)
* [How to: Build Simple Criteria](xref:2132)
* [How to: Build Complex Criteria](xref:2047)

## A Criteria as a String
Anywhere you are required to specify a criteria as a string, you should set a string that can be parsed by the static [CriteriaOperator.Parse](xref:DevExpress.Data.Filtering.CriteriaOperator.Parse*) method. To learn the syntax used in this method, refer to the [Criteria Language Syntax](xref:4928) help topic.

The places where you should specify a criteria as a string include properties in the [Model Editor](xref:112582), and attributes and different properties and methods in code.

The following code demonstrates how to set criteria for the [ActionBase.TargetObjectsCriteria](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria) property of an Action. The Controller below makes the Action available when the selected **Task**'s **DueDate** property value is less than or equal to the system's date and time:

# [C#](#tab/tabid-csharp)

```csharp
public partial class MyController : ViewController {
   private void MyController_AfterConstruction(object sender, EventArgs e) {
      TargetObjectType = typeof(Task);
      MyAction.SelectionDependencyType = SelectionDependencyType.RequireMultipleObjects;
      MyAction.TargetObjectsCriteria = "DueDate <= LocalDateTimeNow()";
   }
}
```

***

The following image demonstrates how the **TargetObjectsCriteria** property is specified in the Model Editor:

![WaysToBuildCriteria](~/images/waystobuildcriteria116081.png)

## Get Criteria String via the Criteria Property Editor
XAF provides the following Windows Forms Criteria Property Editors, intended to construct filter criteria visually (see [Criteria Properties](xref:113564)):

* AdvancedCriteriaPropertyEditor
* CriteriaPropertyEditor
* ExtendedCriteriaPropertyEditor
* PopupCriteriaPropertyEditor

These property editors can be used to represent string properties decorated with the [](xref:DevExpress.ExpressApp.Editors.CriteriaOptionsAttribute) attribute. The following image illustrates the **PopupCriteriaPropertyEditor**:

![PopupCriteriaPropertyEditor](~/images/popupcriteriapropertyeditor116165.png)

The corresponding criteria string is:

``[DueDate] <= LocalDateTimeNow() and [Status] = 'Completed'``

The important concept is that the Criteria Property Editors can generate criteria strings containing the XAF-specific [Object Parameters](xref:113278). Such criteria strings cannot be parsed using the [CriteriaOperator.Parse](xref:DevExpress.Data.Filtering.CriteriaOperator.Parse*) method, provided by XPO. You should use the **GetCriteriaOperator** method exposed by the **CriteriaEditorHelper** helper class, to get the corresponding **CriteriaOperator** object:

# [C#](#tab/tabid-csharp)

```csharp
CriteriaOperator criteria = 
    CriteriaEditorHelper.GetCriteriaOperator(criteriaString, dataType, objectSpace);
```

***

Refer to the [How to: Use Criteria Property Editors](xref:113143) topic to see full example.