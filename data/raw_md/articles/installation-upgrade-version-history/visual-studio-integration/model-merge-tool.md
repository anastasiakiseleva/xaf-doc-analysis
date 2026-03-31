---
uid: "113334"
seealso:
- linkId: "113335"
title: Model Merge Tool
---
# Model Merge Tool

With the [Model Editor](xref:112582), you can examine and edit the [Application Model](xref:112580) in a module, application or user differences layer. But, in some scenarios, it can be required to move the Application Model customizations (differences) from one layer to another. For instance, you can customize a certain [view layout](xref:112817) at runtime, and then want to merge these customizations into a module. This topic provides general information on the **Model Merge Tool** that allows you to merge differences into an underlying Application Model layer. To see a step-by-step example of using this tool, refer to the [How to: Merge End-User Customizations into the XAF Solution](xref:113335) topic.

The Model Merge Tool can be invoked from the context menu of a project in a [XAF solution](xref:118045). If a project is a module project, the **Merge Model** command is available. If a project is an application project, then the **Merge User Model…** option is available in addition to **Merge Model**.

![ModelMerge_ProjectMenu](~/images/modelmerge_projectmenu116869.png)

When you select **Merge Model**, the **Model Merge Tool** is invoked for the application model layer of the current project. When you select **Merge User Model**, the **Open** dialog is shown, so you can select an arbitrary XAFML file. Typically, you select a _Model.User.xafml_ file located in the current project output folder.

> [!NOTE]
> It is recommended that you close all open Model Editor tabs in Visual Studio before running the **Model Merge Tool**.

The Model Merge Tool is the dialog window.

![ModelMerge_Dialog](~/images/modelmerge_dialog116870.png)

It contains a nodes tree similar to the one provided by the Model Editor. Each node is accompanied with a checkbox intended to simplify multi-selection. To merge differences, select one or more nodes (nodes with differences are marked bold). Then, select a target in the dropdown below and click **Merge**. If the chosen differences cannot be applied to the selected target, then the following warning is displayed.

![ModelMerge_Warning](~/images/modelmerge_warning116871.png)

You can select another target in this instance and retry. The merging operation can be performed as many times as required. The **Save** button persists changes.

Application administrators can use the Model Merge feature as well.  Of course they have no access to the application source. But they can merge differences into a common model layer that is typically stored in the _Model.xafml_ file in the application folder. This can be done via the **Merge Differences** command available in Model Editor at runtime.

![ModelMerge_Runtime](~/images/modelmerge_runtime116872.png)

So, an administrator can customize a View and then provide it to all users without disturbing the application developer. In this instance, the _Model.xafml_ file must be shared among all end-users. If terminal server deployment is used, this file is shared initially. Otherwise, an administrator needs to re-deploy the _Model.xafml_ file for all users.