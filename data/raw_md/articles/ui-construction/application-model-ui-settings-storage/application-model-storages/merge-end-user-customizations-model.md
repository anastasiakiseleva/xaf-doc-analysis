---
uid: "113335"
seealso: []
title: 'Merge End-User Settings of a WinForms App from Development to Production Environment'
---
# Merge End-User Settings of a WinForms App from Development to Production Environment

End-users can customize an XAF application user interface (UI) at runtime with ease. The Layout Manager, Column Chooser and other capabilities allow end-users to configure a UI in a "what you see is what you get" way. But when you, as a developer, customize a UI in the [Model Editor](xref:112582), you have to deal with indexes, widths, heights, groups, etc. So, you may want to customize a UI as an end-user, and then merge changes to one of the [Application Model](xref:112580) layers in your XAF solution. This topic describes how to achieve this task using the [Model Merge Tool](xref:113334). As an example, the column order settings will be merged from user differences into the [module project](xref:118045) layer. However, you can use the same approach to merge any end-user customizations. For example:

* List View columns visibility, width, grouping, filter settings;
* Dashboard and Detail View [layouts](xref:112817);
* [Chart](xref:113302) and [Pivot](xref:113303) settings.

> [!NOTE]
> The Model Merge Tool supports only WinForms applications with end-user Model Differences stored in an XAFML file.

## Customize a UI at Run Time
In this topic we will use the **MainDemo** application, located in the _[!include[PathToMainDemo](~/templates/path-to-main-demo-ef-core.md)]_ folder. Open the MainDemo solution, set **MainDemo.Win** as the startup project and run the Windows Forms application. Select the **Resume** navigation item. You will see the **Resume** object's List View. Use drag-and-drop to swap the **File** column with **Contact**.

![ModelMerge_HowTo_SwapColumns](~/images/modelmerge_howto_swapcolumns116862.png)

Close the Windows Forms application. The customizations you have made are saved to the _Model.User.xafml_ file located in the project output folder (_bin\Debug\_ by default).

# [XML](#tab/tabid-xml)

```XML
<ListView Id="Resume_ListView">
  <Columns>
    <ColumnInfo Id="Contact" Index="0" />
    <ColumnInfo Id="File" Index="1" />
  </Columns>
</ListView>
```

***

## Merge User Differences into the Module Project Layer
Now let us merge the end-user customizations into the Application Model of the module project. In the **Solution Explorer**, right click the **MainDemo.Win** application project and click **Merge User Model**. In the invoked **Open** dialog, choose the _Model.User.xafml_ file.

![ModelMerge_HowTo_MergeUserModel](~/images/modelmerge_howto_mergeusermodel116864.png)

As a result, the **Model Merge Tool** dialog is invoked. Navigate to the **Resume_ListView** node in the tree list. This node caption is displayed in bold, as the node contains customizations. Use the checkbox to the left to select this node. In the dropdown below, select **MainDemo.Module** and click **Merge**. The **Resume_ListView** node's differences will be merged into the **MainDemo.Module** project.

![ModelMerge_HowTo_MergeDialog](~/images/modelmerge_howto_mergedialog116865.png)

Finally, click **Save** to persist changes and close the **Model Merge Tool** dialog.

> [!NOTE]
> * You can select several nodes at once, and repeat the merging operation as many times as required, before clicking **Save**. If a part of the selected differences cannot be applied to the selected target, a warning message will be displayed. In this instance, you can try another target (e.g. **MainDemo.Module.Win**).
> * If your application is already deployed, and one of end-users has a carefully crafted layout, you may want to use this layout in a new version of the application. In this instance, just copy the _Model.User.xafml_ file from the end-user workstation, and select this file in the **Open** dialog when running the **Model Merge Tool**.

## Check Changes
After merging, you can see the **Resume_ListView** node customizations in the Model Editor invoked for the **MainDemo.Module** project.

![ModelMerge_HowTo_ME](~/images/modelmerge_howto_me116866.png)

To test changes at run time, reset the user model differences. The simplest way to do this is to delete the _Model.User.xafml_ file from your application project output folder. Then, run the Windows Forms application to see that a layout is customized as required.

![ModelMerge_HowTo_Win](~/images/modelmerge_howto_win116868.png)
