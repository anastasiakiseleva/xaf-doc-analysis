---
uid: "113646"
seealso:
- linkId: "5184"
title: Create and View Reports in a WinForms Application
---
# Create and View Reports in a WinForms Application

This topic describes how an end-user can create and view a report at runtime in a WinForms application. 

## Copy a Predefined Report

Copy a predefined report using the **Copy Predefined Report** (![btn_Copy_Report](~/images/btn_copy_report117441.png)) button and then edit it.

![ReportsV2_CopyPredefined](~/images/reportsv2_copypredefined.png)

## Create a New Report from Scratch

To create a report at runtime, do the following.

* Choose the **Reports** item in the [Navigation](xref:113198).
* Click **New**.
* In the invoked [Report Wizard](xref:4254) dialog, specify the following and click **Next**.
	
	* **Display Name** - the report's name.
	* **Data Type** - the business object type to be used in the report. Only the types that have the [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) or [](xref:DevExpress.Persistent.Base.VisibleInReportsAttribute) attribute applied can be chosen.

    ![ReportsV2_Wizard](~/images/reportsv2_wizard117388.png)

* Choose the [report type](xref:117397).
	
	![ReportsV2_Wizard_Type](~/images/reportsv2_wizard_type.png)
* Follow the wizard's prompts to select report columns, and specify other settings.

Finally, the new report will be opened in the [Report Designer](xref:4256), which provides advanced report layout customization options.

![ReportsV2_Designer](~/images/reportsv2_designer117389.png)

You can see that the data source component has already been added. The data source's ObjectTypeName property is set to the business object type specified in the first page of the **Report Wizard**.

When the **VisibleInReports** attribute is applied to a business class property, it specifies whether or not the target property is visible in the [Report Designer field list](xref:4259). In the **Report Designer**, you can modify the existing fields layout and add more fields.

After a report is saved in the designer, it is added to the **Reports** List View. You can double-click a report to preview it in a [Print Preview Form](xref:5184).

![ReportsV2_Preview](~/images/reportsv2_preview117390.png)