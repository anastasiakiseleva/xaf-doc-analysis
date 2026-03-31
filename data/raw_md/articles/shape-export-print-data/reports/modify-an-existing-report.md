---
uid: "113647"
seealso: []
title: Modify an Existing Report
---
# Modify an Existing Report

This topic describes how an and-user can modify an existing report layout.

## Modify a Report Created at Runtime

Windows Forms
:   Right-click a report and choose **Edit in Designer**.

    ![ShowReportDesigner](~/images/showreportdesigner117394.png)

ASP.NET Core Blazor
:   Select a report and click **Show Report Designer**.

    ![ReportsV2_ShowReportDesigner_Blazor](~/images/ReportsV2_ShowReportDesigner_Blazor.png)

> [!Note]
> ASP.NET Core Blazor Report Designer supports only desktop browsers.

As a result, the new report will be opened in the [WinForms Reporting](xref:1198) or [ASP.NET Core](xref:400249) report designer. Make required modifications and click **Save** to persist report layout changes to the application database.

## Modify a Predefined Static Report
Predefined reports cannot be modified directly (the **Show Report Designer**/**Edit in Designer** action is inactive when the selected report is predefined). However, you can use the existing predefined report as a template for a new report. Right-click the existing predefined report and choose **Copy Predefined Report** (![btn_Copy_Report](~/images/btn_copy_report117441.png)). As a result, an editable copy will be created and you will be able to use the **Show Report Designer**/**Edit in Designer** to open the new report in the Report Designer.