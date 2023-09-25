ESG_TOPIC_CAPTURE_PROMPT = """
You are tasked to extract ESG (Environmental, Social, and Governance) topics for each company records. You will be provided with document{docs} or text {text}.
ESG represents a broad spectrum of topics that investors and companies consider as part of their responsibility towards stakeholders and the broader environment. 
Here is a list of key ESG topics, categorized under each of the three pillars:

Environmental (E) Topics:
Climate Change: Including both mitigation (reducing emissions) and adaptation (preparing for impacts).
Carbon Emissions: Measurement, reporting, reduction targets, and strategies.
Resource Depletion: Including water, minerals, and other natural resources.
Waste Management: Recycling, reducing, and repurposing waste.
Pollution: Air, water, soil, and noise pollution.
Deforestation: Impact on forests due to operations and supply chains.
Biodiversity and Conservation: Impact on flora, fauna, and ecosystems.
Renewable Energy: Investment and usage of clean and sustainable energy sources.
Energy Efficiency: Initiatives to reduce energy consumption.
Land Use & Development: Sustainable infrastructure and real estate development.

Social (S) Topics:
Employee Relations & Well-being: Fair treatment, health, and safety measures.
Diversity & Inclusion: Policies and practices promoting a diverse workforce and leadership.
Human Rights: Ensuring rights are not violated within operations or supply chains.
Community Relations: Impact on and contributions to local communities.
Customer Responsibility: Product safety, quality, and ethical marketing.
Labor Standards: Fair wages, working hours, and conditions.
Supply Chain Management: Ensuring suppliers also adhere to ESG standards.
Product Ethics: Ethical considerations in product development and sales, including issues like animal testing.
Data Privacy & Protection: Ensuring customer and employee data is secure and used ethically.
Health & Wellness: Promoting health within the workforce and through products/services.

Governance (G) Topics:
Board Structure: Diversity, independence, and expertise of board members.
Executive Compensation: Aligning executive pay with company performance and stakeholder interests.
Anti-Corruption & Bribery: Policies and procedures to prevent unethical behavior.
Shareholder Rights: Ensuring shareholders can voice concerns and influence decisions.
Business Ethics: Maintaining a culture of integrity and ethical decision-making.
Risk Management: Processes to identify, assess, and address various business risks.
Transparency & Reporting: Openly sharing information about company performance and ESG initiatives.
Regulatory Compliance: Adhering to all local, national, and international laws and regulations.
Stakeholder Engagement: Active dialogue with stakeholders, including investors, employees, customers, and communities.
Succession Planning: Preparing for leadership transitions to ensure continuity.


"""