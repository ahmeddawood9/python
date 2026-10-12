"""
Lab 04: Intelligent Agents
File: lab04_intelligent_agents.py

Codes in this file (in order):
  1. SimpleReflexAgent     - rules, no memory
  2. ModelBasedReflexAgent - remembers temperature trend
  3. GoalBasedAgent        - moves until goal reached
  4. UtilityBasedAgent     - weighted score, picks best route
  5. LearningAgent         - explore, reward, update knowledge
  6. TASK 1 TrafficLightAgent
  7. TASK 2 SmartLightAgent
  8. TASK 3 DeliveryRobot
  9. TASK 4 Restaurant utility picker (asks for weights)
"""

import random

# ---------- 1. SIMPLE REFLEX: fixed rules, no memory ----------
class SimpleReflexAgent:
    def __init__(self):
        self.rules = {
            'hot': 'Turn ON air conditioning',
            'cold': 'Turn ON heater',
            'comfortable': 'Do nothing (temperature is fine)'
        }

    def sense(self, temperature):
        if temperature > 75:
            return 'hot'
        elif temperature < 65:
            return 'cold'
        else:
            return 'comfortable'

    def act(self, percept):
        return self.rules.get(percept, 'Do nothing')

    def run(self, temperature):
        percept = self.sense(temperature)
        action = self.act(percept)
        print(f'Temperature: {temperature}F -> Percept: {percept} -> Action: {action}')

agent = SimpleReflexAgent()
agent.run(80)
agent.run(60)
agent.run(70)


# ---------- 2. MODEL-BASED REFLEX: remembers state (trend) ----------
class ModelBasedReflexAgent:
    def __init__(self):
        self.state = {'previous_temp': None, 'trend': 'stable'}

    def update_state(self, temperature):
        if self.state['previous_temp'] is not None:
            if temperature > self.state['previous_temp']:
                self.state['trend'] = 'rising'
            elif temperature < self.state['previous_temp']:
                self.state['trend'] = 'falling'
            else:
                self.state['trend'] = 'stable'
        self.state['previous_temp'] = temperature

    def act(self, temperature):
        self.update_state(temperature)
        if temperature > 75:
            return 'Turn ON AC (it is hot)'
        elif temperature > 70 and self.state['trend'] == 'rising':
            return 'Turn ON AC early (temperature is rising!)'
        elif temperature < 65:
            return 'Turn ON heater'
        else:
            return 'Do nothing'

    def run(self, temperature):
        action = self.act(temperature)
        trend = self.state['trend']
        print(f'Temp: {temperature}F | Trend: {trend} | Action: {action}')

agent = ModelBasedReflexAgent()
for temp in [68, 70, 72, 74, 76]:
    agent.run(temp)


# ---------- 3. GOAL-BASED: moves until the goal is reached ----------
class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def sense(self, position):
        return position

    def decide(self, percept):
        if percept < self.goal:
            return "Move Right"
        elif percept > self.goal:
            return "Move Left"
        else:
            return "Goal Reached"

    def act(self, action, current_position):
        if action == "Move Right":
            return current_position + 1
        elif action == "Move Left":
            return current_position - 1
        else:
            return current_position

    def run(self, start_position):
        position = start_position
        print(f"Starting at position {position}")
        print(f"Goal is {self.goal}")
        while True:
            percept = self.sense(position)
            action = self.decide(percept)
            print(f"Position: {position} -> Action: {action}")
            if action == "Goal Reached":
                break
            position = self.act(action, position)
        print("Goal achieved!")

agent = GoalBasedAgent(goal=5)
agent.run(start_position=1)


# ---------- 4. UTILITY-BASED: score every option, pick the highest ----------
class UtilityBasedAgent:
    def __init__(self):
        self.weights = {'time': 0.4, 'cost': 0.3, 'safety': 0.3}   # must sum to 1

    def utility(self, route):
        score = 0
        for factor, weight in self.weights.items():
            score += route[factor] * weight
        return round(score, 2)

    def choose_best(self, routes):
        print('Evaluating routes...')
        best_route = None
        best_score = -1
        for name, route in routes.items():
            score = self.utility(route)
            print(f'  {name}: time={route["time"]}, cost={route["cost"]}, '
                  f'safety={route["safety"]} -> Utility = {score}')
            if score > best_score:
                best_score = score
                best_route = name
        print(f'Best choice: {best_route} (utility = {best_score})')

routes = {
    'Highway':  {'time': 7, 'cost': 8,  'safety': 6},
    'Motorway': {'time': 9, 'cost': 5,  'safety': 9},
    'Scenic':   {'time': 4, 'cost': 10, 'safety': 7},
}
agent = UtilityBasedAgent()
agent.choose_best(routes)          # Motorway wins with 7.8


# ---------- 5. LEARNING AGENT: explore, get reward, update knowledge ----------
class LearningAgent:
    def __init__(self, actions):
        self.actions = actions
        self.knowledge = {a: 0 for a in actions}   # start knowing nothing
        self.exploration_rate = 0.3                # 30% chance to try something new

    def performance_element(self):
        if random.random() < self.exploration_rate:
            return random.choice(self.actions)     # Problem Generator: explore
        return max(self.knowledge, key=self.knowledge.get)   # best known

    def critic(self, action, reward):
        return reward

    def learning_element(self, action, reward):
        self.knowledge[action] = round(
            self.knowledge[action] * 0.7 + reward * 0.3, 2)

    def run(self, reward_function, steps=10):
        for step in range(1, steps + 1):
            action = self.performance_element()
            reward = reward_function(action)
            self.critic(action, reward)
            self.learning_element(action, reward)
            print(f'Step {step}: Action={action}, Reward={reward}, '
                  f'Knowledge={self.knowledge}')

def food_reward(food):
    rewards = {'Apple': 8, 'Candy': 3, 'Salad': 9, 'Chips': 2}
    return rewards[food] + random.randint(-1, 1)

random.seed(42)
agent = LearningAgent(['Apple', 'Candy', 'Salad', 'Chips'])
agent.run(food_reward, steps=8)


# ============================================================
# LAB TASKS
# ============================================================
# ---------- TASK 1: Simple Reflex, traffic light ----------
class TrafficLightAgent:
    def __init__(self):
        self.rules = {'green': 'GO', 'yellow': 'SLOW DOWN', 'red': 'STOP'}
    def act(self, light):
        return self.rules.get(light, 'Unknown light')

agent = TrafficLightAgent()
for light in ["green", "red", "yellow", "green", "red"]:
    print(light, "->", agent.act(light))


# ---------- TASK 2: Model-Based, smart room light ----------
class SmartLightAgent:
    def __init__(self):
        self.state = {'empty_minutes': 0, 'occupied': False}

    def update_state(self, occupied):
        self.state['occupied'] = occupied
        if occupied:
            self.state['empty_minutes'] = 0
        else:
            self.state['empty_minutes'] += 1     # one reading = one minute

    def act(self, occupied, is_dark):
        self.update_state(occupied)
        if not is_dark:
            return "Lights OFF (bright daytime)"
        if self.state['empty_minutes'] >= 5:
            return "Lights OFF (empty 5+ minutes)"
        if self.state['occupied'] and is_dark:
            return "Lights ON"
        return "Lights OFF"

agent = SmartLightAgent()
print(agent.act(True, True))                     # ON
for _ in range(6):
    print(agent.act(False, True))                # OFF after 5 empty minutes
print(agent.act(True, False))                    # OFF, bright


# ---------- TASK 3: Goal-Based, delivery robot A -> D ----------
class DeliveryRobot:
    def __init__(self, goal, graph):
        self.goal = goal
        self.graph = graph
    def run(self, start):
        location = start
        print("Start at", location)
        while location != self.goal:
            # choose the move that is the goal if possible, else the first move
            moves = self.graph[location]
            nxt = self.goal if self.goal in moves else moves[0]
            print(f"Move {location} -> {nxt}")
            location = nxt
        print("Package Delivered")

graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
DeliveryRobot('D', graph).run('A')


# ---------- TASK 4: Utility-Based, restaurant picker ----------
restaurants = {
    'Restaurant A': {'taste': 8, 'price': 6, 'distance': 7, 'hygiene': 9},
    'Restaurant B': {'taste': 9, 'price': 8, 'distance': 5, 'hygiene': 8},
    'Restaurant C': {'taste': 7, 'price': 9, 'distance': 9, 'hygiene': 7},
    'Restaurant D': {'taste': 8, 'price': 7, 'distance': 6, 'hygiene': 10},
}

weights = {}
for factor in ['taste', 'price', 'distance', 'hygiene']:
    weights[factor] = float(input(f"Enter {factor.title()} Weight: "))

if abs(sum(weights.values()) - 1.0) > 1e-9:
    print("Weights must add up to 1.0")
else:
    best_name, best_utility = None, -1
    for name, scores in restaurants.items():
        utility = sum(scores[f] * weights[f] for f in weights)
        print(f"{name} -> Utility: {round(utility, 2)}")
        if utility > best_utility:
            best_name, best_utility = name, utility
    print("Best Restaurant:", best_name)
    print("Highest Utility:", round(best_utility, 2))
# weights 0.4, 0.2, 0.1, 0.3 give A=7.8, B=8.1, C=7.6, D=8.2 -> D wins
