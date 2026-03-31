---
uid: "113333"
seealso: []
title: Model Editor Settings
---
# Model Editor Settings

The Model Editor saves its settings between runs (the currently focused node, search pane configuration, etc.). This topic lists the settings storages used by the Model Editor in different circumstances.

| How the Model Editor was Invoked | Settings Storage |
|---|---|
| From a Windows Forms **XAF** application, via the **EditModel** Action. | The _Model.User.xafml_ file under the hidden **ModelEditorSettings** node. |
| As a standalone utility. | The system registry _HKEY_CURRENT_USER\Software\Developer Express\XAF\Model Editor_ key. |
| As a Visual Studio designer. | The solution user options (_SUO_) file. |
