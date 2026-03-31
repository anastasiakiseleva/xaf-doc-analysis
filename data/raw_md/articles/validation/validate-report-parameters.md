---
uid: "113259"
seealso:
- linkId: "113251"
- linkId: "112649"
title: Validate Report Parameters
---
# Validate Report Parameters
You can require end users to specify report parameters when reports are viewed with a [filtered data source](xref:113594):

![Validation_NonPersistent](~/images/validation_nonpersistent127814.png)

You can use the solution described below to validate these parameters.

* Implement a [](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase) class descendant and set the report's [IReportDataV2.ParametersObjectType](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2.ParametersObjectType) property to your custom type. See the following help topic for details: [Data Filtering in Reports V2](xref:113594).
* Apply a validation rule to the required property. Set the rule's custom validation context to "PreviewReport". This can be done either in code, or in the [Model Editor](xref:112582). See the following help topic for details: [Declare Validation Rules](xref:113251).
* The report parameter validation should be performed when the Preview action is executed. Navigate to the **ActionDesign** |  **Actions** | **PreviewReportV2** node in the **Model Editor**, and set the **ValidationContexts** property to "PreviewReport".

The following code snippet illustrates the **ReportParametersObjectBase** class descendant. Its **ShowTasksAssignedTo** property is decorated by [](xref:DevExpress.Persistent.Validation.RuleRequiredFieldAttribute).

# [C#](#tab/tabid-csharp)

```csharp
[DomainComponent]
public class MyReportParametersObject : ReportParametersObjectBase {
    public MyReportParametersObject(IObjectSpaceCreator provider) : 
        base(provider) { }
    public override CriteriaOperator GetCriteria() {
        return CriteriaOperator.Parse("[FullName] = '" + showTasksAssignedTo.FullName + "'");
    }
    public override SortProperty[] GetSorting() {
        List<SortProperty> sorting = new List<SortProperty>();
        return sorting.ToArray();
    }
    protected override IObjectSpace CreateObjectSpace() {
        return objectSpaceCreator.CreateObjectSpace(typeof(Contact));
    }
    private Contact showTasksAssignedTo;
    [RuleRequiredField("RuleRequiredField for MyReportParametersObject", "PreviewReport", 
        "Assigned To cannot be empty")]
    public Contact ShowTasksAssignedTo {
        get {
            return showTasksAssignedTo;
        }
        set {
            showTasksAssignedTo = value;
        }
    }
}
```
***

The following image illustrates the rule's node in the Model Editor.

![Validation_NonPersistent_ME](~/images/validation_nonpersistent_me116609.png)

The following image shows the broken rule detection.

![Validation_NonPersistent_Report](~/images/validation_nonpersistent_report116611.png)

