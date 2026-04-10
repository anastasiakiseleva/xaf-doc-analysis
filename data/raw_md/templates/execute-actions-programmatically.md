We do not recommend that you use the `DoExecute` and other methods to execute Actions because such methods can contain UI-specific code. You can refactor your Action's event handlers and extract the required code into separate methods. Call these separate methods directly without triggering UI-related Action code.

Programmatic execution of custom and built-in Actions is acceptable in rare advanced scenarios, for example, if you:
* Create a custom Action Container and call the `DoExecute` method inside the Action control. In this context, you have complete control over your custom code and can execute any action. Remember to trigger life-cycle events for your actions (such as `Execute`).
* Add new ways to invoke Actions from the UI (for example, support keyboard or voice control).
* Reuse a built-in Action in a specific context where you would need to write a lot of code to re-implement the Action's internal business logic.

For more information on how to implement such complex requirements, refer to the following materials:
* [XAF - How to execute Actions programmatically](https://github.com/DevExpress-Examples/xaf-how-to-execute-actions-in-code).
<:0:>
<:1:>