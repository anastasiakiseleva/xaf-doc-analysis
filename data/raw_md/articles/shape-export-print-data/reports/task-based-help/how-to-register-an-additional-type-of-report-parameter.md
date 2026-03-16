---
uid: "113609"
seealso: []
title: 'How to: Register an Additional Type of XtraReport Parameter'
owner: Ekaterina Kiseleva
---
# How to: Register an Additional Type of XtraReport Parameter

This example demonstrates how to extend the list of parameter types available in the **Report Designer**.

[!include[ReportsV2ExampleNote](~/templates/reportsv2examplenote111131.md)]

Access an **XtraReportDataTypeProvider** instance using the **XafReportDataTypeProvider** parameter passed to the static **ReportDesignExtensionManager.CustomizeReportExtension** event. Then, handle the **XtraReportDataTypeProvider.CustomAddParameterTypes** event and add custom types to the **Dictionary** list passed to the event handler. Additionally, handle the **XtraReportDataTypeProvider.GetCustomEditableDataTypes** event and add custom types to the **Types** array passed to the event handler. The following snippet illustrates how to add the **Gender** enumeration type.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.ReportsV2;
// ...
static class Program {
    static void Main() {
        ReportDesignExtensionManager.CustomizeReportExtension += ReportDesignExtensionManager_CustomizeReportExtension;
        // ...
    }
    static void ReportDesignExtensionManager_CustomizeReportExtension(object sender, CustomizeReportExtensionEventArgs e) {
        e.XafReportDataTypeProvider.CustomAddParameterTypes += XafReportDataTypeProvider_CustomAddParameterTypes;
        e.XafReportDataTypeProvider.GetCustomEditableDataTypes += XafReportDataTypeProvider_GetCustomEditableDataTypes;
    }
    static void XafReportDataTypeProvider_CustomAddParameterTypes(object sender, AddCustomParameterTypesEventArgs e) {
        e.Dictionary.Add(typeof(Gender), "Gender");
    }
    static void XafReportDataTypeProvider_GetCustomEditableDataTypes(object sender, GetCustomEditableDataTypesEventArgs e) {
        List<Type> types = new List<Type>(e.Types);
        types.Add(typeof(Gender));
        e.Types = types.ToArray();
    }
    // ...
}
public enum Gender { Male, Female}
```
***

The result is demonstrated in the image below.

![ReportsV2_CustomAddParameterTypes](~/images/reportsv2_customaddparametertypes117417.png)