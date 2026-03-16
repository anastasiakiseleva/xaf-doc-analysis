---
uid: "113691"
seealso:
- linkId: "113690"
title: Notifications Localization
owner: Anastasiya Kisialeva
---
# Notifications Localization

This topic describes how to localize texts used in [Notifications Window Elements](xref:113692) (form caption, columns captions, Actions captions, and the **Snooze time** combo box).

![Notifications_AlertWindow](~/images/notifications_alertwindow117584.png)

> [!NOTE]
> Before you proceed, we recommend that you review the [Localization Basics](xref:112595) topic for information about UI element localization in the [Model Editor](xref:112830).

## Step-by-Step Instructions

1. Start the Model Editor for the module project and select the target language in the **Languages** combo box.

2. Expand the **ActionDesign** | **Actions** node. Translate **Caption** values for the following Actions.
	
	* **Dismiss**
	* **DismissAll**
	* **RefreshNotifications**
	* **Snooze**
	* **SnoozeListAction**
3. Expand the **BOModel** | **Notification** | **OwnMembers** node. Translate **Caption** values for the following members.
	
	* **AlarmTime**
	* **State**
	* **Subject**
4. Expand the **BOModel** | **PostponeTime** | **OwnMembers** node. Translate **Caption** value for the **RemindIn** member.
5. Expand the **Localization** | **Notifications** node. Translate **Value** texts for the following **LocalizationItem** nodes.
	
	* **NotificationViewCaption**
	* **ShowPostponedItemsActionDisabledTooltip**
	* **ShowPostponedItemsActionEnabledTooltip**
6. Expand the **Localization** | **NotificationsPostponeTimesList** node. Translate **Value** texts for all **LocalizationItem** child nodes.
6. Navigate to the **Views** | **NotificationsObject_DetailView** | **Items** | **Postpone** node. Translate the **Caption** value.