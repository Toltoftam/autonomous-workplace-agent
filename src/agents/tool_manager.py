class ToolManager:

    AVAILABLE_TOOLS = [

        "email_sender",

        "report_generator",

        "crm_lookup",

        "lead_search"
    ]

    def get_tools(self):

        return self.AVAILABLE_TOOLS

    def has_tool(
        self,
        tool_name
    ):

        return (
            tool_name
            in self.AVAILABLE_TOOLS
        )
