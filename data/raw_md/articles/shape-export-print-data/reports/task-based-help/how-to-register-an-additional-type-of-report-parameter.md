---
uid: "113609"
seealso: []
title: 'How to: Register an Additional Type of XtraReport Parameter'
---
# How to: Register an Additional Type of XtraReport Parameter

This example demonstrates how to extend the list of parameter types available in the Report Designer.

[!include[ReportsV2ExampleNote](~/templates/reportsv2examplenote111131.md)]

1. Handle the static `ReportDesignExtensionManager.CustomizeReportExtension` event to access an `XtraReportDataTypeProvider` instance. 
1. Handle the `XtraReportDataTypeProvider.CustomAddParameterTypes` event to add custom types to the `Dictionary` list. 
1. Handle the `XtraReportDataTypeProvider.GetCustomEditableDataTypes` event to add custom types to the `Types` array. 

The following code snippet illustrates how to add the `Gender` enumeration type.

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

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp.ReportsV2
' ...
Friend NotInheritable Class Program
    Private Sub New()
    End Sub
    Shared Sub Main()
        AddHandler ReportDesignExtensionManager.CustomizeReportExtension, AddressOf ReportDesignExtensionManager_CustomizeReportExtension
        ' ...
    End Sub
    Private Shared Sub ReportDesignExtensionManager_CustomizeReportExtension(ByVal sender As Object, ByVal e As CustomizeReportExtensionEventArgs)
        AddHandler e.XafReportDataTypeProvider.CustomAddParameterTypes, AddressOf XafReportDataTypeProvider_CustomAddParameterTypes
        AddHandler e.XafReportDataTypeProvider.GetCustomEditableDataTypes, AddressOf XafReportDataTypeProvider_GetCustomEditableDataTypes
    End Sub
    Private Shared Sub XafReportDataTypeProvider_CustomAddParameterTypes(ByVal sender As Object, ByVal e As AddCustomParameterTypesEventArgs)
        e.Dictionary.Add(GetType(Gender), "Gender")
    End Sub
    Private Shared Sub XafReportDataTypeProvider_GetCustomEditableDataTypes(ByVal sender As Object, ByVal e As GetCustomEditableDataTypesEventArgs)
        Dim types As New List(Of Type)(e.Types)
        types.Add(GetType(Gender))
        e.Types = types.ToArray()
    End Sub
    ' ...
End Class
Public Enum Gender
    Male
    Female
End Enum
```

***

The result is demonstrated in the image below.

![ReportsV2_CustomAddParameterTypes](~/images/reportsv2_customaddparametertypes117417.png)