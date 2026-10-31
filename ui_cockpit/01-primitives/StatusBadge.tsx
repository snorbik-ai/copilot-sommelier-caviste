import React from 'react';

export interface StatusBadgeProps {
  status: 'PENDING' | 'VALIDATED' | 'WARNING';
  label: string;
}

export const StatusBadge: React.FC<StatusBadgeProps> = ({ status, label }) => {
  const colorMap = {
    PENDING: '#f59e0b',
    VALIDATED: '#10b981',
    WARNING: '#ef4444'
  };
  return (
    <span style={{ backgroundColor: colorMap[status], color: '#fff', padding: '4px 8px', borderRadius: 4, fontSize: 12 }}>
      {label}
    </span>
  );
};
