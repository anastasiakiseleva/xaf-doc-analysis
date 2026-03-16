---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Criteria
name: Criteria
type: Property
summary: Specifies the criteria string used when determining whether [AppearanceAttribute.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.TargetItems) should be affected by the conditional appearance rule generated from the current attribute.
syntax:
  content: public string Criteria { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string representing the criterion under which the conditional appearance rule is in effect.
seealso:
- linkId: "113286"
---
To learn how to declare string criteria and use Function Criteria Operators in string criteria, refer to the following topics:

- [Ways to Build Criteria](xref:113052);
- [Function Criteria Operators](xref:113307).

When you need to create a complex rule that cannot be specified in the `Criteria` property, you can implement a business class method that takes no parameters and returns a Boolean value that specifies whether the rule is active. XAF ignores the `Criteria` property in this case. You do not need to specify the `Method` parameter if you apply [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute) directly to the business class method. For more information, refer to the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Method) property description.

### Delayed Loading and Free Joins in Criteria Expressions

Avoid [Delayed Properties](xref:2024) and [Free Joins](xref:8130) in a criteria expression, because @DevExpress.ExpressApp.ConditionalAppearance.AppearanceController calculates the expression during the paint process. 

> [!NOTE]
> In Windows Forms applications, Delayed Properties and Free Joins may load data from the database during the paint process. This may cause UI flicks or corrupt the state of a Windows Forms control.

Use the following techniques to avoid side effects if you need to include Delayed Properties in a criteria expression:

- Add a calculated property to a business object and store the calculated value in the database. For additional information refer to the following topic: [](xref:113179).
- Use the @DevExpress.ExpressApp.BaseObjectSpace.SetPrefetchPropertyNames(System.Object,System.String[]) method to pre-load collection properties before displaying data on the screen. 

If the above techniques are not applicable and your app crashes with `InvalidOperationException` ('Recursive read not allowed' or 'Entering the GetObjectsNonReenterant state is prohibited'), use the solution #4 from the following article: [Troubleshooting - How to resolve the "Entering the 'GetObjectsNonReenterant' state..." error](https://supportcenter.devexpress.com/ticket/details/k18167/troubleshooting-how-to-resolve-the-entering-the-getobjectsnonreenterant-state-error).

## Examples

### Example 1

[!include[ConditionalFormatting_CategoryColoredInListViewRule](~/templates/conditionalformatting_categorycoloredinlistviewrule11918.md)]

### Example 2

[!include[ConditionalFormatting_ActionVisibility](~/templates/conditionalformatting_actionvisibility11919.md)]

For additional examples, refer to following topic: [Declare Conditional Appearance Rules in Code](xref:113371).

[!include[<`Appearance` attribute>](~/templates/main-demo-tip.md)]