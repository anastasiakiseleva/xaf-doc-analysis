---
uid: DevExpress.Persistent.Base.ActionAttribute
name: ActionAttribute
type: Class
summary: Converts a persistent class method into a [SimpleAction](xref:112622) or [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction).
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Method)]
    public class ActionAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.ActionAttribute._members
  altText: ActionAttribute Members
---
An Action can be implemented in a persistent class declaration. When the **Action** attribute is applied to a persistent class method, a new Action is added to the special built-in **ObjectMethodActionsViewController** [View Controller](xref:112621). If the target method is parameterless, then a SimpleAction is created. If this method takes a [non-persistent object](xref:116516) as a parameter, then a PopupWindowShowAction is created, and a passed object's Detail View is shown in a pop-up. When this Action is executed, the target method is called. The target method's declaring class is assigned to the Action's [ActionBase.TargetObjectType](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectType) property. So, this Action is activated only for objects of the specified type. When activated, this Action is displayed within the **RecordsEdit** Action Container, because the [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property of these Actions is set to "RecordEdit", by default. You can override this behavior by passing the required category as the _category_ parameter. You can also specify other named parameters to define the Action's details: caption, tooltip, image name and so on.

Identifiers (see [ActionBase.Id](xref:DevExpress.ExpressApp.Actions.ActionBase.Id)) of Actions declared via the **Action** attribute are formed by combining the declaring type name and target method name separated with a dot. If target method takes a parameter, then the method parameter type name is also appended. For instance, if the **Action** attribute is applied to a **Recalculate** method declared in an **Order** business class, the resulting Action's identifier will be "Order.Recalculate". Metadata information on the Actions is available in the [Application Model](xref:112580). So, just like with a regular Action declared in a Controller, you can customize these Actions via **ActionDesign** | **Action** node properties in the [Model Editor](xref:112830).

> [!NOTE]
> 
> @DevExpress.Persistent.Base.ActionAttribute is primarily used in simple scenarios only when you execute logic based on data available within the business class context (for instance, modify class properties). @DevExpress.Persistent.Base.ActionAttribute is NOT suitable for any UI-related logic and complex user interactions. It is also NOT possible to access @DevExpress.ExpressApp.XafApplication, [Views](xref:112611), and other XAF UI-related entities within the business class code, because it violates the [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) principle and is against the [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) architecture (your data model should not be tied to the UI). To access @DevExpress.ExpressApp.XafApplication, [Views](xref:112611), and other UI-related entities, implement [Controllers](xref:112621) with [Actions](xref:112622).

If the **Action** attribute's parameters do not allow you to define a particular feature, add a Simple Action to a custom Controller in the standard way (see [](xref:402157), [](xref:402158)).

To see an example of the **Action** attribute in use, refer to the [How to: Create an Action Using the Action Attribute](xref:112619) topic.

> [!TIP]
> It is not recommended to create actions within business classes because normally, a business model is separated from UI settings.