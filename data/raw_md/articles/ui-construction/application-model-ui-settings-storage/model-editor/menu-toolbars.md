---
uid: "113327"
seealso: []
title: Menu Toolbars
owner: Ekaterina Kiseleva
---
# Menu Toolbars

The [Model Editor](xref:112582) includes a toolbar that can be displayed at design time and at runtime. This topic describes the functionality in both cases.

## Design Time Toolbar

The image below illustrates the toolbar that is available at design time.

![|DevExpress XAF Model Editor: Design-Time Toolbar](~/images/localizationtoolbar115643.png)


| Command | Shortcut | Description |
|---|---|---|
| ![DevExpress XAF Model Editor: Reload](~/images/Action_Reload.png)&nbsp;**Reload** | CTRL+R | Cancels all unsaved changes made within the Model Editor. |
| ![DevExpress XAF Model Editor: Back](~/images/Action_Navigation_History_Back.png)&nbsp;**Back** | - | Navigates to the previously focused node. |
| ![DevExpress XAF Model Editor: Forward](~/images/Action_Navigation_History_Forward.png)&nbsp;**Forward** | - | Cancels the **Back** command. |
| **Language** | - | Specifies the current language aspect. For details, refer to the [Localization Basics](xref:112595) topic. |
| ![DevExpress XAF Model Editor: Localization](~/images/BO_Localization.png)&nbsp;**Localization** | - | Invokes the [Localization Tool](xref:113297). |
| ![DevExpress XAF Model Editor: Show Links/Hide Links](~/images/ModelEditor_Links.png)&nbsp;**Show&nbsp;Links&nbsp;/&nbsp;Hide&nbsp;Links** | - | Toggles the Linked Nodes visibility in the [Nodes Tree](xref:113328). |
| ![DevExpress XAF Model Editor: Loaded Modules](~/images/ModelEditor_Action_Modules.png)&nbsp;**Loaded&nbsp;Modules** | - | Displays a list of [modules](xref:118046) used to generate the current content of the Application Model. |
| ![DevExpress XAF Model Editor: Search](~/images/Action_Search.png)&nbsp;**Search** | CTRL+ALT+F | Invokes a [Search Pane](xref:113331). |
| ![DevExpress XAF Model Editor: Show Unusable Data](~/images/ModelEditor_ShowUnusableNodes.png)&nbsp;**Show&nbsp;Unusable&nbsp;Data** | - | Displays the XML code of unusable nodes (nodes absent in the actual model, but customized in an XAFML file). You usually encounter unusable nodes after upgrading your application to use updated (newer) modules. For more information, refer to the following topic: [](xref:119123). |


To save changes made within the Model Editor at design time, use the Visual Studio **Save** button or CTRL+S shortcut.


## Runtime and Standalone Menu Toolbar

The image below illustrates the toolbar that is available when the Model Editor [is invoked](xref:113326) as a standalone tool.

![|DevExpress XAF Model Editor: Standalone Toolbar](~/images/modeleditor_toolbar115350.png)

| Button/Action | Shortcut | Description |
|---|---|---|
| ![DevExpress XAF Model Editor: Open](~/images/Action_Open.png)&nbsp;**Open** | CTRL+O | **(Available in standalone Model Editor only)** Opens the Application Model of a specific XAF application or module. |
| ![DevExpress XAF Model Editor: Save](~/images/Action_Save.png)&nbsp;**Save** | CTRL+S | Saves changes made within the Model Editor to the user differences. |
| ![DevExpress XAF Model Editor: Reload](~/images/Action_Reload.png)&nbsp;**Reload** | CTRL+R | Cancels all unsaved changes made within the Model Editor. |
| ![DevExpress XAF Model Editor: Merge Differences](~/images/ModelEditor_ModelMerge.png)&nbsp;**Merge&nbsp;Differences** | - | **(Available in runtime only)** Merges the current node(s) differences into the underlying model layer. See the [Model Merge Tool](xref:113334) topic for details. |
| **Language** | - | Specifies the current language aspect. For details, refer to the [Localization Basics](xref:112595) topic. |
| ![DevExpress XAF Model Editor: Localization](~/images/BO_Localization.png)&nbsp;**Localization** | - | Invokes the [Localization Tool](xref:113297). |
| ![DevExpress XAF Model Editor: Back](~/images/Action_Navigation_History_Back.png)&nbsp;**Back** | ALT+LEFT | Navigates to the previously focused node. |
| ![DevExpress XAF Model Editor: Forward](~/images/Action_Navigation_History_Forward.png)&nbsp;**Forward** | ALT+RIGHT | Cancels the **Back** action. |
| ![DevExpress XAF Model Editor: Show Links/Hide Links](~/images/ModelEditor_Links.png)&nbsp;**Show&nbsp;Links&nbsp;/&nbsp;Hide&nbsp;Links** | - | Toggles the Linked Nodes visibility in the [Nodes Tree](xref:113328). |
| ![DevExpress XAF Model Editor: Loaded Modules](~/images/ModelEditor_Action_Modules.png)&nbsp;**Loaded&nbsp;Modules** | - | Displays a list of [modules](xref:118046) used to generate the current content of the Application Model. |
| ![DevExpress XAF Model Editor: Search](~/images/Action_Search.png)&nbsp;**Search** | CTRL+ALT+F | Invokes a [Search Pane](xref:113331). |
| ![DevExpress XAF Model Editor: Show Unusable Data](~/images/ModelEditor_ShowUnusableNodes.png)&nbsp;**Show&nbsp;Unusable&nbsp;Data** | - | Displays the XML code of unusable nodes (nodes absent in the actual model, but customized in an XAFML file). You usually encounter unusable nodes after upgrading your application to use updated (newer) modules. For more information, refer to the following topic: [](xref:119123). |

## Limitations

XAF uses a single Visual Studio extension for all versions. As a result, the Model Editor toolbar is not supported in .NET projects created for previous versions after you install XAF v22.1 or later.
