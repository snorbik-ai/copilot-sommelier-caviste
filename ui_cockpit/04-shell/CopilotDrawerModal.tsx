import React from 'react';
import { CopilotChatPanel } from '../02-features/CopilotChatPanel';

export const CopilotDrawerModal: React.FC<{ isOpen: boolean; onClose: () => void; apiEndpoint: string }> = ({ isOpen, onClose, apiEndpoint }) => {
  if (!isOpen) return null;
  return (
    <div style={{ position: 'fixed', right: 0, top: 0, bottom: 0, width: 400, backgroundColor: '#fff', boxShadow: '-2px 0 8px rgba(0,0,0,0.15)', zIndex: 1000, padding: 16 }}>
      <button onClick={onClose} style={{ float: 'right', border: 'none', background: 'transparent', cursor: 'pointer', fontSize: 16 }}>✕</button>
      <CopilotChatPanel apiEndpoint={apiEndpoint} />
    </div>
  );
};
